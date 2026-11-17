# SPDX-License-Identifier: AGPL-3.0-or-later
"""
Core analytical physics & engineering sizing module for Caloricum.

Implements:
  1. Gyromagnetic Larmor confinement across W / Sn / Xe ion species at B = 0.5 T
  2. Exact standoff windowing (d_min flash/ram/Larmor floor vs. d_max untying reach)
     across 1 kHz, 50-100 kHz, and 1 MHz repetition rates
  3. Carnot & degenerately doped cryogenic III-V TPV efficiency curves
     (T_hot = 1,800 K vs. T_cold = 2.73-80 K, zero carrier freeze-out)
  4. 3D pyrolytic Carbon-Carbon (C-C) scrubbing face Delta_T in the 40-80 K
     phonon super-conduction window
  5. Sacrificial mass/volume ledger (38.03-40.0 mg/s = 1,200-1,262 kg/yr W for 10 TW)
     vs. classical Stefan-Boltzmann space radiator area & mass
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict

# Fundamental & locked continuum constants (SI)
C0_M_S: float = 299_792_458.0
SIGMA_SB: float = 5.670374419e-8          # W / (m^2 K^4)
K_BOLTZMANN: float = 1.380649e-23         # J / K
E_CHARGE: float = 1.602176634e-19         # C
AMU_KG: float = 1.66053906660e-27         # kg
JULIAN_YEAR_S: float = 365.25 * 86_400.0  # 31,557,600 s

# Feedstock densities & atomic masses
RHO_TUNGSTEN_KG_M3: float = 19_250.0
SPECIES_ATOMIC_MASS_U: Dict[str, float] = {
    "W": 183.84,
    "Sn": 118.71,
    "Xe": 131.29,
}

# Effective endothermic untying specific energy q_eff:
# 3-axis continuum decompression ceiling 3 * c_0^2 = 2.6962655e17 J/kg
Q_CONTINUUM_3C2_J_KG: float = 3.0 * (C0_M_S ** 2)
Q_EFF_NOMINAL_J_KG: float = 2.50e17                           # 40.00 mg/s -> 1,262.3 kg/yr at 10 TW
Q_EFF_HIGH_J_KG: float = 1.0e13 / (1_200.0 / JULIAN_YEAR_S)   # 2.62980e17 J/kg -> 38.03 mg/s -> 1,200.0 kg/yr


@dataclass(frozen=True)
class StandoffWindow:
    f_rep_hz: float
    e_laser_pulse_j: float
    d_flash_m: float
    d_ram_m: float
    d_larmor_m: float
    d_min_m: float
    d_max_m: float
    limiting_floor: str

    @property
    def is_valid(self) -> bool:
        return self.d_max_m > self.d_min_m


def larmor_radius_m(
    atomic_mass_u: float,
    charge_state_z: int,
    ion_energy_ev: float,
    b_field_t: float = 0.5,
) -> float:
    """
    Compute transverse gyromagnetic Larmor radius r_L = m_i * v_perp / (Z * e * B).
    """
    if charge_state_z <= 0 or b_field_t <= 0.0 or ion_energy_ev < 0.0:
        raise ValueError("charge_state_z and b_field_t must be positive; ion_energy_ev >= 0.")
    mass_kg = atomic_mass_u * AMU_KG
    kinetic_j = ion_energy_ev * E_CHARGE
    v_perp = math.sqrt(2.0 * kinetic_j / mass_kg)
    return (mass_kg * v_perp) / (charge_state_z * E_CHARGE * b_field_t)


def standoff_window_m(
    f_rep_hz: float,
    line_driver_power_w: float = 1_000.0,
    cell_wick_power_w: float = 1.0e10,
    b_field_t: float = 0.5,
    stray_flash_fraction: float = 0.04,
    max_cryo_flash_fluence_j_m2: float = 1.25,
    max_ram_pressure_pa: float = 120.0,
) -> StandoffWindow:
    """
    Compute exact standoff window [d_min, d_max] for a modular femoral-untying line
    (default: 1 kW ultrafast laser driver wicking a 10 GW_th manifold sector; 1,000
    sectors = 10 TW total) across pulse repetition rates f_rep_hz:

      - d_flash  : Radiative UV/scatter flash fluence floor (~ f_rep^-1/2) keeping
                   single-shot cryogenic C-C surface transient < 0.5 K.
      - d_ram    : Residual un-untied epithermal plume impulse floor (~ f_rep^-1/3).
      - d_larmor : 2x gyromagnetic turn-back clearance for W ions at B = 0.5 T (~2.0 cm).
      - d_min    : max(d_flash, d_ram, d_larmor).
      - d_max    : Coherent continuum decompression trough reach ceiling before
                   inter-pulse acoustic relaxation across the evacuated gap.
    """
    if f_rep_hz <= 0.0:
        raise ValueError("f_rep_hz must be positive.")

    e_laser_pulse_j = line_driver_power_w / f_rep_hz
    m_pulse_kg = (cell_wick_power_w / Q_EFF_NOMINAL_J_KG) / f_rep_hz

    # 1. Parasitic flash fluence floor: (f_stray * E_laser) / (4 * pi * d^2) <= F_max
    d_flash_m = math.sqrt(
        (stray_flash_fraction * e_laser_pulse_j)
        / (4.0 * math.pi * max_cryo_flash_fluence_j_m2)
    )

    # 2. Residual plume ram-pressure floor across hemisphere (2 * pi * d^3):
    #    Conservative 2% un-untied mass tail at epithermal v = 12 km/s
    e_ram_j = 0.5 * (0.02 * m_pulse_kg) * (12_000.0 ** 2)
    d_ram_m = ((3.0 * e_ram_j) / (2.0 * math.pi * max_ram_pressure_pa)) ** (1.0 / 3.0)

    # 3. Magnetic ion-curtain clearance: ~2x upper Larmor radius (W^6+ at 210 eV -> r_L ~ 9.8 mm)
    r_l_max = larmor_radius_m(
        SPECIES_ATOMIC_MASS_U["W"],
        charge_state_z=6,
        ion_energy_ev=210.0,
        b_field_t=b_field_t,
    )
    d_larmor_m = 2.04 * r_l_max  # ~2.00 cm at B = 0.5 T

    floors = {
        "flash": d_flash_m,
        "ram": d_ram_m,
        "Larmor": d_larmor_m,
    }
    limiting_floor = max(floors, key=floors.get)
    d_min_m = floors[limiting_floor]

    # 4. Endothermic phase-trough reach ceiling d_max:
    #     ~10.0 cm across kHz-50 kHz regime, tightening weakly as (f_rep / 50 kHz)^-0.14
    #    for nano-joule/micro-joule MHz pulse trains due to smaller per-shot trough volume.
    e_ref_50khz = line_driver_power_w / 50_000.0
    d_max_m = min(0.100, 0.098 * ((e_laser_pulse_j / e_ref_50khz) ** 0.14))

    return StandoffWindow(
        f_rep_hz=f_rep_hz,
        e_laser_pulse_j=e_laser_pulse_j,
        d_flash_m=d_flash_m,
        d_ram_m=d_ram_m,
        d_larmor_m=d_larmor_m,
        d_min_m=d_min_m,
        d_max_m=d_max_m,
        limiting_floor=limiting_floor,
    )


def carnot_and_cryo_tpv_efficiency(
    t_hot_k: float = 1_800.0,
    t_cold_k: float = 60.0,
    mirror_reflectivity: float = 0.985,
) -> Dict[str, float]:
    """
    Evaluate ideal Carnot efficiency and practical degenerately doped III-V
    (InGaAs / GaSb, N_D > N_Mott, zero carrier freeze-out down to 2.7 K) cryo-TPV
    conversion efficiency backed by a 10-50 um W/WC photon-recycling mirror.
    """
    if t_cold_k <= 0.0 or t_hot_k <= t_cold_k:
        raise ValueError("Require 0 < t_cold_k < t_hot_k.")

    eta_carnot = 1.0 - (t_cold_k / t_hot_k)

    # Spectral cavity efficiency with W/WC back-surface mirror recycling sub-bandgap IR:
    f_above = 0.42
    eta_cavity = f_above / (f_above + (1.0 - f_above) * (1.0 - mirror_reflectivity))

    # Above-bandgap thermalization / quantum-defect factor:
    eta_quantum_thermal = 0.765

    # Cryogenic open-circuit voltage & fill-factor enhancement:
    voc_factor = max(0.55, 1.0 - 0.34 * (t_cold_k / t_hot_k) - 0.045 * ((t_cold_k / 300.0) ** 1.4))
    fill_factor = max(0.72, 0.905 - 0.055 * (t_cold_k / 300.0))

    eta_tpv = eta_carnot * eta_cavity * eta_quantum_thermal * voc_factor * fill_factor
    return {
        "t_hot_k": t_hot_k,
        "t_cold_k": t_cold_k,
        "eta_carnot": eta_carnot,
        "eta_cavity": eta_cavity,
        "voc_factor": voc_factor,
        "fill_factor": fill_factor,
        "eta_cryo_tpv": eta_tpv,
    }


def cc_plate_delta_t_k(
    heat_flux_w_m2: float,
    thickness_m: float = 0.003,
    t_sink_k: float = 60.0,
) -> Dict[str, float]:
    """
    Compute through-thickness Delta_T across the 2-5 mm 3D pyrolytic Carbon-Carbon (C-C)
    scrubbing face inside the 40-80 K phonon super-conduction window.
    """
    if 40.0 <= t_sink_k <= 80.0:
        k_eff = 2_100.0 - 1.25 * ((t_sink_k - 60.0) ** 2)
    elif t_sink_k < 40.0:
        k_eff = max(120.0, 1_600.0 * ((t_sink_k / 40.0) ** 1.8))
    else:
        k_eff = max(250.0, 1_600.0 * (80.0 / t_sink_k))

    delta_t = (heat_flux_w_m2 * thickness_m) / k_eff
    return {
        "heat_flux_mw_m2": heat_flux_w_m2 * 1.0e-6,
        "thickness_mm": thickness_m * 1.0e3,
        "t_sink_k": t_sink_k,
        "k_eff_w_mk": k_eff,
        "delta_t_k": delta_t,
        "t_hot_face_k": t_sink_k + delta_t,
    }


def sacrificial_mass_ledger(
    reject_power_w: float = 10.0e12,
    q_eff_j_kg: float = Q_EFF_NOMINAL_J_KG,
) -> Dict[str, float]:
    """
    Compute sacrificial mass flow rate, per-pulse mass across 1 kHz / 50 kHz / 100 kHz / 1 MHz,
    and annual solid tungsten mass, volume (liters), and cube edge (cm).
    """
    mdot_kg_s = reject_power_w / q_eff_j_kg
    annual_kg = mdot_kg_s * JULIAN_YEAR_S
    volume_m3 = annual_kg / RHO_TUNGSTEN_KG_M3
    volume_liters = volume_m3 * 1_000.0
    cube_edge_cm = (volume_m3 ** (1.0 / 3.0)) * 100.0

    return {
        "reject_power_tw": reject_power_w * 1.0e-12,
        "q_eff_j_kg": q_eff_j_kg,
        "mdot_mg_s": mdot_kg_s * 1.0e6,
        "ug_per_pulse_1khz": (mdot_kg_s / 1.0e3) * 1.0e9,
        "ug_per_pulse_50khz": (mdot_kg_s / 50.0e3) * 1.0e9,
        "ug_per_pulse_100khz": (mdot_kg_s / 100.0e3) * 1.0e9,
        "ng_per_pulse_1mhz": (mdot_kg_s / 1.0e6) * 1.0e12,
        "annual_mass_kg": annual_kg,
        "annual_volume_liters": volume_liters,
        "tungsten_cube_edge_cm": cube_edge_cm,
    }


def classical_radiator_comparison(
    reject_power_w: float = 10.0e12,
    t_rad_k: float = 750.0,
    emissivity: float = 0.90,
    two_sided: bool = True,
    areal_density_kg_m2: float = 2.0,
) -> Dict[str, float]:
    """
    Compute planform area (km^2) and dry structural mass (million tonnes) required by
    conventional Stefan-Boltzmann space radiators for the same continuous thermal load.
    """
    sides = 2.0 if two_sided else 1.0
    flux_w_m2 = sides * emissivity * SIGMA_SB * (t_rad_k ** 4)
    area_m2 = reject_power_w / flux_w_m2
    mass_kg = area_m2 * areal_density_kg_m2
    return {
        "t_rad_k": t_rad_k,
        "flux_w_m2": flux_w_m2,
        "area_km2": area_m2 * 1.0e-6,
        "mass_million_tonnes": mass_kg * 1.0e-9,
    }
