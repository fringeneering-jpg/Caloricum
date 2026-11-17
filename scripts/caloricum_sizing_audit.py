#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""
caloricum_sizing_audit.py — Standalone Sizing & Thermodynamic Verification Suite
Repository : https://github.com/fringeneering-jpg/Caloricum
Master DOI : https://doi.org/10.5281/zenodo.24281039
Dependencies: Python 3 standard library (+ optional numpy check)

Computes and verifies:
  1. 0.5 T parallel magnetic ion-curtain Larmor radii (r_L ~ 3-11 mm, zero sputtering)
  2. Exact standoff windows (d_min flash/ram/Larmor floor vs. d_max reach ceiling)
     across 1 kHz, 50-100 kHz, and 1 MHz repetition rates
  3. Carnot & degenerately doped III-V cryo-TPV efficiency curves
     (T_hot = 1,800 K vs. T_cold = 2.73-80 K, compared with 500-750 K radiators)
  4. 2-5 mm 3D pyrolytic Carbon-Carbon (C-C) scrubbing face Delta_T
  5. Annual tungsten mass/volume ledger (38.03-40.0 mg/s = 1,200-1,262 kg/yr,
     62.3-65.6 L, ~40 cm cube) vs. 310-1,568 km^2 (0.62-3.14 Mt) classical radiators
"""

from __future__ import annotations

import os
import sys

# Ensure repository root is importable regardless of working directory
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

try:
    import numpy as np  # Optional stdlib/numpy verification
    HAS_NUMPY = True
except ImportError:
    np = None  # type: ignore[assignment]
    HAS_NUMPY = False

from caloricum.core import (
    Q_CONTINUUM_3C2_J_KG,
    Q_EFF_HIGH_J_KG,
    Q_EFF_NOMINAL_J_KG,
    SPECIES_ATOMIC_MASS_U,
    carnot_and_cryo_tpv_efficiency,
    cc_plate_delta_t_k,
    classical_radiator_comparison,
    larmor_radius_m,
    sacrificial_mass_ledger,
    standoff_window_m,
)


def main() -> int:
    banner = "=" * 86
    print(banner)
    print(" CALORICUM PULSED-UNTYING CRYO-COOLING CORE — SIZING & THERMODYNAMIC AUDIT")
    print(" Foundational Theory DOI: https://doi.org/10.5281/zenodo.24281039")
    print(f" Runtime Backend        : Python {sys.version.split()[0]} "
          f"({'NumPy ' + np.__version__ if HAS_NUMPY else 'Pure Stdlib'})")
    print(banner)

    # ------------------------------------------------------------------
    # 1. Magnetic Ion-Deflection Curtain Audit (B = 0.5 T)
    # ------------------------------------------------------------------
    print("\n[1] 0.5 T PARALLEL MAGNETIC ION-CURTAIN LARMOR CONFINEMENT (ZERO WALL SPUTTERING)")
    print("-" * 86)
    ion_cases = [
        ("Sn", 1, 1.2, "Epithermal singly ionized Sn+ tail"),
        ("Xe", 1, 1.5, "Epithermal singly ionized Xe+ tail"),
        ("W", 10, 55.0, "Cold tunnel-stripped W10+ nominal"),
        ("W", 8, 120.0, "Cold tunnel-stripped W8+ intermediate"),
        ("W", 6, 230.0, "Upper-tail tunnel-stripped W6+"),
    ]
    print(f"{'Species':<8} {'Z':>4} {'E_ion (eV)':>12} {'B (T)':>8} {'r_L (mm)':>12}  Regime")
    r_l_values_mm = []
    for sym, z_val, e_ev, note in ion_cases:
        r_mm = larmor_radius_m(SPECIES_ATOMIC_MASS_U[sym], z_val, e_ev, b_field_t=0.5) * 1.0e3
        r_l_values_mm.append(r_mm)
        print(f"{sym:<8} {z_val:>4d} {e_ev:>12.1f} {0.5:>8.2f} {r_mm:>12.2f}  {note}")
        assert 2.5 <= r_mm <= 11.5, f"Larmor radius {r_mm:.2f} mm outside 3-11 mm design band!"

    # ------------------------------------------------------------------
    # 2. Standoff Window Audit Across Repetition Rates
    # ------------------------------------------------------------------
    print("\n[2] MICRO-MANIFOLD STANDOFF WINDOWS (d_min FLOOR vs. d_max UNTYING REACH)")
    print("-" * 86)
    rep_rates = [
        (1.0e3, "1 kHz (high-energy pulse)"),
        (50.0e3, "50 kHz (nominal sweet spot)"),
        (100.0e3, "100 kHz (high-rep nominal)"),
        (1.0e6, "1 MHz (compact MHz train)"),
    ]
    print(f"{'Rep Rate':<28} {'d_flash':>9} {'d_ram':>9} {'d_Larmor':>9} "
          f"{'d_min':>9} {'d_max':>9}  Limiting Floor")
    for f_hz, label in rep_rates:
        win = standoff_window_m(f_hz)
        print(
            f"{label:<28} "
            f"{win.d_flash_m * 100:>7.2f}cm "
            f"{win.d_ram_m * 100:>7.2f}cm "
            f"{win.d_larmor_m * 100:>7.2f}cm "
            f"{win.d_min_m * 100:>7.2f}cm "
            f"{win.d_max_m * 100:>7.2f}cm  {win.limiting_floor}"
        )
        assert win.is_valid, f"Invalid standoff window at {label}"

    # ------------------------------------------------------------------
    # 3. Carnot & Degenerately Doped III-V Cryo-TPV Efficiency Curves
    # ------------------------------------------------------------------
    print("\n[3] CARNOT & DEGENERATELY DOPED III-V CRYO-TPV EFFICIENCY (T_hot = 1,800 K)")
    print("-" * 86)
    t_cold_grid = [2.73, 4.20, 20.0, 40.0, 60.0, 80.0, 500.0, 750.0]
    if HAS_NUMPY:
        t_cold_iter = np.array(t_cold_grid, dtype=float).tolist()
    else:
        t_cold_iter = t_cold_grid

    print(f"{'T_cold (K)':>10} {'Carnot (%)':>12} {'Cavity (%)':>12} "
          f"{'V_oc Fac':>10} {'FF':>8} {'Net TPV (%)':>13}  Operating Band")
    for tc in t_cold_iter:
        res = carnot_and_cryo_tpv_efficiency(t_hot_k=1_800.0, t_cold_k=tc)
        if tc <= 4.5:
            band = "Deep cryo (zero freeze-out N_D > N_Mott)"
        elif 40.0 <= tc <= 80.0:
            band = "Phonon super-conduction window [TARGET]"
        elif tc < 40.0:
            band = "Sub-40 K cryogenic transition"
        else:
            band = "Classical space-radiator sink (degraded)"
        print(
            f"{tc:>10.2f} "
            f"{res['eta_carnot'] * 100:>11.2f}% "
            f"{res['eta_cavity'] * 100:>11.2f}% "
            f"{res['voc_factor']:>10.3f} "
            f"{res['fill_factor']:>8.3f} "
            f"{res['eta_cryo_tpv'] * 100:>12.2f}%  {band}"
        )
        if tc <= 80.0:
            assert res["eta_carnot"] > 0.955 and res["eta_cryo_tpv"] > 0.60

    # ------------------------------------------------------------------
    # 4. 3D Pyrolytic Carbon-Carbon (C-C) Scrubbing Face Delta_T
    # ------------------------------------------------------------------
    print("\n[4] 3D PYROLYTIC CARBON-CARBON (C-C) SCRUBBING PLATE DELTA_T (T_sink = 60 K)")
    print("-" * 86)
    cc_cases = [
        (0.5e6, 0.002),
        (1.0e6, 0.003),
        (5.0e6, 0.003),
        (10.0e6, 0.003),
        (10.0e6, 0.005),
    ]
    print(f"{'Flux (MW/m^2)':>14} {'Thickness (mm)':>15} {'k_eff (W/mK)':>14} "
          f"{'Delta_T (K)':>13} {'T_hot_face (K)':>16}")
    for q_flux, thick_m in cc_cases:
        cc = cc_plate_delta_t_k(q_flux, thickness_m=thick_m, t_sink_k=60.0)
        print(
            f"{cc['heat_flux_mw_m2']:>14.2f} "
            f"{cc['thickness_mm']:>15.1f} "
            f"{cc['k_eff_w_mk']:>14.1f} "
            f"{cc['delta_t_k']:>13.2f} "
            f"{cc['t_hot_face_k']:>16.2f}"
        )
        assert cc["t_hot_face_k"] < 90.0, "C-C plate exited cryogenic window!"

    # ------------------------------------------------------------------
    # 5. 10 TW Sacrificial Tungsten Ledger vs. Classical Space Radiators
    # ------------------------------------------------------------------
    print("\n[5] 10 TW CONTINUOUS HEAT-REJECTION LEDGER: CALORICUM vs. CLASSICAL RADIATORS")
    print("-" * 86)
    led_low_mass = sacrificial_mass_ledger(10.0e12, q_eff_j_kg=Q_EFF_HIGH_J_KG)
    led_high_mass = sacrificial_mass_ledger(10.0e12, q_eff_j_kg=Q_EFF_NOMINAL_J_KG)

    print(f"Continuum 3*c_0^2 ceiling           : {Q_CONTINUUM_3C2_J_KG:.4e} J/kg")
    print(f"Effective untying enthalpy q_eff    : {led_high_mass['q_eff_j_kg']:.3e} - "
          f"{led_low_mass['q_eff_j_kg']:.3e} J/kg")
    print(f"Continuous sacrificial feed (mdot)  : {led_low_mass['mdot_mg_s']:.2f} - "
          f"{led_high_mass['mdot_mg_s']:.2f} mg/s")
    print(f"Per-pulse feed at  1 kHz            : {led_low_mass['ug_per_pulse_1khz']:.2f} - "
          f"{led_high_mass['ug_per_pulse_1khz']:.2f} ug/pulse")
    print(f"Per-pulse feed at 50 kHz            : {led_low_mass['ug_per_pulse_50khz']:.3f} - "
          f"{led_high_mass['ug_per_pulse_50khz']:.3f} ug/pulse")
    print(f"Per-pulse feed at  1 MHz            : {led_low_mass['ng_per_pulse_1mhz']:.2f} - "
          f"{led_high_mass['ng_per_pulse_1mhz']:.2f} ng/pulse")
    print(f"Annual consumable tungsten mass     : {led_low_mass['annual_mass_kg']:,.1f} - "
          f"{led_high_mass['annual_mass_kg']:,.1f} kg/yr")
    print(f"Annual solid tungsten volume        : {led_low_mass['annual_volume_liters']:.2f} - "
          f"{led_high_mass['annual_volume_liters']:.2f} liters/yr")
    print(f"Equivalent solid tungsten cube edge : {led_low_mass['tungsten_cube_edge_cm']:.2f} - "
          f"{led_high_mass['tungsten_cube_edge_cm']:.2f} cm (~40 cm cube)")

    rad_750 = classical_radiator_comparison(10.0e12, t_rad_k=750.0)
    rad_500 = classical_radiator_comparison(10.0e12, t_rad_k=500.0)
    print("-" * 86)
    print(f"Classical Space Radiator @ 750 K    : {rad_750['area_km2']:,.1f} km^2  |  "
          f"{rad_750['mass_million_tonnes']:.2f} million tonnes (at 2.0 kg/m^2)")
    print(f"Classical Space Radiator @ 500 K    : {rad_500['area_km2']:,.1f} km^2  |  "
          f"{rad_500['mass_million_tonnes']:.2f} million tonnes (at 2.0 kg/m^2)")
    mass_advantage = (rad_750["mass_million_tonnes"] * 1.0e9) / led_high_mass["annual_mass_kg"]
    print(f"Annual Consumable Mass Advantage    : {mass_advantage:,.0f}x lighter than dry 750 K radiator array")

    # Strict self-consistency assertions
    assert 38.0 <= led_low_mass["mdot_mg_s"] <= 38.1
    assert 39.9 <= led_high_mass["mdot_mg_s"] <= 40.1
    assert 1_199.9 <= led_low_mass["annual_mass_kg"] <= 1_200.1
    assert 1_262.0 <= led_high_mass["annual_mass_kg"] <= 1_263.0
    assert 62.2 <= led_low_mass["annual_volume_liters"] <= 62.5
    assert 65.4 <= led_high_mass["annual_volume_liters"] <= 65.7
    assert 309.0 <= rad_750["area_km2"] <= 311.0
    assert 1_567.0 <= rad_500["area_km2"] <= 1_569.0

    print("\n" + banner)
    print(" ALL CALORICUM SIZING & THERMODYNAMIC CHECKS PASSED (EXIT 0)")
    print(banner)
    return 0


if __name__ == "__main__":
    sys.exit(main())
