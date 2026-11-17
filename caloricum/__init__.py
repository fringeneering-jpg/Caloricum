# SPDX-License-Identifier: AGPL-3.0-or-later
"""
Caloricum — Standalone Pulsed-Untying Cryo-Cooling Core
Software licensed under GNU AGPLv3 (see LICENSE-AGPLv3.txt).
Hardware geometries licensed under CERN-OHL-S v2 (see LICENSE-CERN-OHL-S-v2.txt).
Master Theory DOI: https://doi.org/10.5281/zenodo.24281039
"""

from .core import (
    AMU_KG,
    C0_M_S,
    E_CHARGE,
    JULIAN_YEAR_S,
    K_BOLTZMANN,
    Q_CONTINUUM_3C2_J_KG,
    Q_EFF_HIGH_J_KG,
    Q_EFF_NOMINAL_J_KG,
    RHO_TUNGSTEN_KG_M3,
    SIGMA_SB,
    SPECIES_ATOMIC_MASS_U,
    StandoffWindow,
    carnot_and_cryo_tpv_efficiency,
    cc_plate_delta_t_k,
    classical_radiator_comparison,
    larmor_radius_m,
    sacrificial_mass_ledger,
    standoff_window_m,
)

__all__ = [
    "AMU_KG",
    "C0_M_S",
    "E_CHARGE",
    "JULIAN_YEAR_S",
    "K_BOLTZMANN",
    "Q_CONTINUUM_3C2_J_KG",
    "Q_EFF_HIGH_J_KG",
    "Q_EFF_NOMINAL_J_KG",
    "RHO_TUNGSTEN_KG_M3",
    "SIGMA_SB",
    "SPECIES_ATOMIC_MASS_U",
    "StandoffWindow",
    "carnot_and_cryo_tpv_efficiency",
    "cc_plate_delta_t_k",
    "classical_radiator_comparison",
    "larmor_radius_m",
    "sacrificial_mass_ledger",
    "standoff_window_m",
]
