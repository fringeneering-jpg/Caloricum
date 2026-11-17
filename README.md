# Caloricum: Standalone Pulsed-Untying Cryo-Cooling Core

[![Master Theory DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24281039.svg)](https://doi.org/10.5281/zenodo.24281039)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--4121--4296-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0005-4121-4296)
[![Software License: GNU AGPLv3](https://img.shields.io/badge/Code-GNU%20AGPLv3-blue.svg)](./LICENSE-AGPLv3.txt)
[![Hardware License: CERN-OHL-S v2](https://img.shields.io/badge/Hardware-CERN--OHL--S%20v2-orange.svg)](./LICENSE-CERN-OHL-S-v2.txt)

**`Caloricum`** is an open-source, dual-copylefted high-flux **endothermic thermal-vacuum core** derived from the continuum mass-energy mechanics ($m = L/c_0^2$) of [**Phase Wave Cosmology (PWC)**](https://doi.org/10.5281/zenodo.24281039). Instead of rejecting waste heat across square kilometers of fragile Stefan–Boltzmann radiative fins ($q'' = \varepsilon\sigma T^4$), `Caloricum` couples a cryogenic degenerately doped III-V thermophotovoltaic (TPV) thermal diode stack into a compact evacuated micro-manifold where transverse **cold femtosecond tunnel ionization** unbinds dense sacrificial matter (`W` / `Sn` / `Xe`) into the electromagnetic plenum at an effective endothermic heat-wicking capacity of **$q_{\text{eff}} \approx 2.5 \times 10^{17}\text{ J/kg}$**.

`Caloricum` serves as the standalone thermal-rejection core imported by [**Prometheus**](https://github.com/fringeneering-jpg/Prometheus) (planetary $40\text{ TW}$ solar-laser & zero-brine desalination grid) and scales modularly across **orbital power conversion**, **tokamak/fission divertors**, **hypersonic reentry leading edges**, **AI/HPC data centers**, and **high-output prime movers**.

---

## 1. Executive Physical Overview

Conventional thermal engineering treats vacuum as an insulator limited by fourth-power blackbody photon emission ($\sigma T^4$). Under Phase Wave Cosmology ([DOI: `10.5281/zenodo.24281039`](https://doi.org/10.5281/zenodo.24281039)), baryonic rest mass is confined electromagnetic wave energy locked at the nuclear acoustic ceiling ($\rho_{\max} = 1.304 \times 10^{15}\text{ kg/m}^3$) inside the ambient continuum plenum ($\rho_0 = 8.74 \times 10^{-27}\text{ kg/m}^3$, **"heat hates pressure"**).

- **Cold Femtosecond Tunnel Ionization ($\tau_p \le 100\text{ fs}$, $I = 10^{15}\text{–}10^{16}\text{ W/cm}^2$):**  
  An ultrashort laser beam fires **transversely (parallel to the cold scrubbing wall)** across a micron-scale sacrificial wire or synchronized micro-droplet/cluster feed (`W`, `Sn`, or `Xe`) inside an evacuated manifold ($0.1\text{–}10\text{ mTorr}$ terrestrial vacuum jacket or open space). Because the pulse duration ($\le 100\text{ fs}$) is two orders of magnitude shorter than the electron–phonon lattice thermalization time ($\tau_{\text{e-ph}} \sim 1\text{–}10\text{ ps}$) and operates deep in the optical-field tunneling regime (Keldysh parameter $\gamma_K \ll 1$), barrier-suppression stripping occurs **cold**—avoiding classical nanosecond hydrodynamic plasma heating and thermal bremsstrahlung flash.
- **Endothermic Continuum Decompression ($q_{\text{eff}} \approx 2.5 \times 10^{17}\text{ J/kg}$):**  
  Sudden non-thermal knot unbinding creates an acute local phase-pressure trough across a **$2\text{–}10\text{ cm}$ standoff zone**, drawing phonon/thermal energy out of the adjacent cryogenic Carbon-Carbon (`C-C`) scrubbing face at up to $q_{\text{eff}} \approx 2.50\text{–}2.63 \times 10^{17}\text{ J/kg}$ ($\approx 93\text{–}97.5\%$ of the 3-axis continuum decompression ceiling $3 c_0^2 = 2.70 \times 10^{17}\text{ J/kg}$).

---

## 2. Core Thermal Diode & Scrubbing Manifold Stack

```text
================================================================================
 [1] HOT LOAD (1,800 K emitter / divertor / reentry skin / engine / server bus)
--------------------------------------------------------------------------------
     ~~~ Radiative / Near-Field Photonic Gap (Vacuum Thermal Isolation) ~~~
--------------------------------------------------------------------------------
 [2] DEGENERATELY DOPED CRYO III-V TPV JUNCTION (InGaAs / GaSb, N_D > N_Mott)
     • Zero carrier freeze-out down to 2.7–4 K
     • Held in 40–80 K ballistic/hydrodynamic phonon super-conduction window
     • Converts >50–65% of incoming thermal flux directly into DC electricity
--------------------------------------------------------------------------------
 [3] 10–50 um W / WC OPTICAL & EM BACKSTOP MIRROR
     • Reflects >98% of sub-bandgap IR photons back to hot emitter (recycling)
     • Shields III-V junction from stray UV/X-ray/RF transients in manifold
--------------------------------------------------------------------------------
 [4] 2–5 mm 3D PYROLYTIC CARBON-CARBON (C-C) SCRUBBING FACE
     • Phonon super-conduction window (40–80 K): k_eff ~ 1,500–2,500 W/(m·K)
     • Minimal through-thickness gradient (Delta_T ~ 1.3–3.3 K at 1 MW/m^2)
--------------------------------------------------------------------------------
 [5] 0.5 T PARALLEL MAGNETIC ION-DEFLECTION CURTAIN (B || wall)
     • Gyromagnetic Larmor radius r_L ~ 3–11 mm << 20–100 mm standoff
     • Deflects 100% of residual W/Sn/Xe ions away from wall (ZERO sputtering)
--------------------------------------------------------------------------------
 [6] 2–10 cm STANDOFF ENDOTHERMIC UNTYING ZONE (0.1–10 mTorr or Open Space)
     • Transverse femtosecond beam (tau_p <= 100 fs, 10^15–10^16 W/cm^2)
     • Sacrificial dense feed (W wire / Sn droplet / Xe cluster): q_eff ~ 2.5e17 J/kg
================================================================================
```

| Layer | Material & Geometry | Operating Regime | Engineering Function |
| :--- | :--- | :--- | :--- |
| **Hot Load** | Refractory emitter / heat exchanger | $T_{\text{hot}} \approx 1,800\text{ K}$ (typ.) | Primary reject-heat interface (solar-laser cavity, divertor, aero shell, or heat-pump bus) |
| **Cryo-TPV Diode** | Degenerately doped `InGaAs` / `GaSb` ($N > 10^{18}\text{–}10^{19}\text{ cm}^{-3}$) | $40\text{–}80\text{ K}$ nominal ($2.7\text{–}4\text{ K}$ floor) | Metallic impurity-band conduction prevents cryogenic carrier freeze-out; near-Carnot $V_{\text{oc}}$ ($\eta_{\text{Carnot}} = 95.6\text{–}99.85\%$) |
| **Backstop Mirror** | $10\text{–}50\text{ }\mu\text{m}$ `W` / `WC` thin film | $40\text{–}80\text{ K}$ | Sub-bandgap IR photon recycling ($\ge 98\%$) + hard electromagnetic/UV shield between untying zone and semiconductor |
| **Scrubbing Face** | $2\text{–}5\text{ mm}$ 3D pyrolytic `C-C` | $40\text{–}80\text{ K}$ phonon peak | Umklapp-suppressed phonon transport wicks heat uniformly into the vacuum untying boundary |
| **Magnetic Curtain** | Parallel $B = 0.5\text{ T}$ (`NdFeB`/`SmCo` or SC) | $r_L \approx 3\text{–}11\text{ mm}$ | Turns back epithermal & multiply ionized residual ions before wall contact (**zero sputtering**) |
| **Untying Zone** | $2\text{–}10\text{ cm}$ standoff; `W` / `Sn` / `Xe` feed | $0.1\text{–}10\text{ mTorr}$ or space | Transverse $\le 100\text{ fs}$ tunnel ionization unbinds mass feed at $q_{\text{eff}} \approx 2.5 \times 10^{17}\text{ J/kg}$ |

---

## 3. Full `10 TW` Reference Operating Ledger vs. Classical Space Radiators

For a planetary-scale **$10\text{ TW}$ ($1.0 \times 10^{13}\text{ W}$) continuous thermal rejection duty** (matching the Stage 1 orbital reject-heat load of [`Prometheus`](https://github.com/fringeneering-jpg/Prometheus)):

| Metric | `Caloricum` Endothermic Core | Classical Stefan–Boltzmann Space Radiators |
| :--- | :--- | :--- |
| **Governing Heat-Sink Law** | $\dot{Q} = \dot{m}\,q_{\text{eff}}$ ($q_{\text{eff}} \approx 2.50\text{–}2.63 \times 10^{17}\text{ J/kg}$) | $\dot{Q} = 2\varepsilon\sigma A T_{\text{rad}}^4$ ($\varepsilon = 0.90$, two-sided panels) |
| **Cold-Sink Temperature ($T_{\text{cold}}$)** | **$40\text{–}80\text{ K}$** (capable down to **$2.73\text{–}4\text{ K}$**) | **$500\text{–}750\text{ K}$** (forced high-$T$ to shrink $T^{-4}$ area) |
| **Continuous Mass Feed ($\dot{m}$)** | **$38.03\text{–}40.00\text{ mg/s}$** | N/A (closed coolant loops susceptible to micrometeoroid puncture) |
| **Per-Pulse Mass ($1\text{ kHz}$)** | **$38.03\text{–}40.00\text{ }\mu\text{g/pulse}$** | — |
| **Per-Pulse Mass ($50\text{ kHz}$)** | **$0.761\text{–}0.800\text{ }\mu\text{g/pulse}$** | — |
| **Per-Pulse Mass ($1\text{ MHz}$)** | **$38.0\text{–}40.0\text{ ng/pulse}$** | — |
| **Annual Consumable Mass ($1\text{ yr}$)** | **$1,200\text{–}1,262\text{ kg/yr}$** (`1.20–1.26 tonnes/yr`) | **$0\text{ kg/yr}$** consumable, **millions of tonnes** dry hardware |
| **Annual Tungsten Volume ($\rho_W = 19,250\text{ kg/m}^3$)** | **$62.3\text{–}65.6\text{ liters/yr}$** (**$\sim 40\text{ cm}$ solid `W` cube**) | **$310\text{–}1,568\text{ km}^2$** panel planform area |
| **System Structural Mass** | **Compact manifold modules** ($< 10^{-5}\times$ radiator mass) | **$0.62\text{–}3.14\text{ million tonnes}$** (at ultra-light $2.0\text{ kg/m}^2$) |
| **Carnot Limit at $T_{\text{hot}} = 1,800\text{ K}$** | **$95.56\%\text{–}99.85\%$** (enables $>50\%$ cryo-TPV recovery) | **$58.3\%\text{–}72.2\%$** (collapses TPV voltage & dark current) |

---

## 4. Target Engineering Domains

1. **Orbital Power Conversion & Directed Solar Grids ([`Prometheus`](https://github.com/fringeneering-jpg/Prometheus)):** Eliminates million-tonne radiator farms on multi-terawatt solar-pumped laser stations while holding III-V TPV recovery diodes at $40\text{–}80\text{ K}$ for $80\%$ net solar-to-coherent optical conversion.
2. **Tokamak / Stellarator & Fission Divertors:** Replaces erosion-limited water/helium cooling channels behind tungsten/C-C divertor cassettes ($10\text{–}20\text{ MW/m}^2$ steady heat flux) with a solid-state `C-C` + `W/WC` + vacuum untying backing jacket.
3. **Hypersonic Reentry Leading Edges:** Integrates a sealed $0.1\text{–}10\text{ mTorr}$ internal micro-manifold behind ultra-high-temperature `C-C`/`WC` stagnation noses, actively wicking aerothermal heating into a gram-scale spooled tungsten wire feed with zero shape-changing external ablation.
4. **High-Density AI/HPC & Quantum Data Centers:** Condenses megawatt-scale rack heat rejection into shoebox-sized sealed vacuum manifolds, simultaneously providing $40\text{–}80\text{ K}$ cryo-bus cooling and recovering $50\%+$ electric power via high-$T$/cryo-TPV stages.
5. **High-Output Aviation, Marine & Industrial Engines:** Eliminates heavy liquid-air heat exchangers and radiator drag while harvesting exhaust enthalpy through compact cryo-TPV diode collars.

---

## 5. Verification Suite & Benchtop Kill-Test

### Run the Analytical Sizing & Thermodynamic Audit (`exit 0`, Python Stdlib / NumPy)
```bash
python scripts/caloricum_sizing_audit.py
```
`scripts/caloricum_sizing_audit.py` (backed by the importable `caloricum` Python package) deterministically computes and audits:
- Exact standoff windows ($d_{\min}$ flash/ram/Larmor floor vs. $d_{\max}$ untying reach ceiling across `1 kHz`, `50 kHz`, `100 kHz`, and `1 MHz`),
- Gyromagnetic Larmor confinement radii ($r_L \approx 3\text{–}11\text{ mm}$ at $B = 0.5\text{ T}$) across epithermal and multiply-charged `W`/`Sn`/`Xe` ions,
- Carnot & degenerately doped `InGaAs`/`GaSb` cryo-TPV efficiency curves ($T_{\text{hot}} = 1,800\text{ K}$ vs. $T_{\text{cold}} = 2.73\text{–}80\text{ K}$),
- 3D pyrolytic `C-C` scrubbing-plate $\Delta T$ across $0.5\text{–}20\text{ MW/m}^2$ wall fluxes, and
- Complete `10 TW` sacrificial `W`/`Sn`/`Xe` mass/volume ledger vs. $310\text{–}1,568\text{ km}^2$ ($0.62\text{–}3.14\text{ Mt}$) classical space radiators.

### Low-Cost Laboratory Falsification Protocol
See **[`docs/BENCHTOP_FALSIFICATION_PROTOCOL.md`](./docs/BENCHTOP_FALSIFICATION_PROTOCOL.md)** for a complete university/garage vacuum bell-jar kill-test ($100\text{ fs}$ kHz laser grazing a `W` wire at $2\text{–}5\text{ cm}$ standoff from a heated `C-C` strip behind a $0.5\text{ T}$ magnet curtain at $0.1\text{–}10\text{ mTorr}$):
- **Classical MHD / Radiation Prediction:** $\Delta T_{\text{strip}} \ge 0$ (net radiative/bremsstrahlung heating).
- **PWC Endothermic Untying Prediction:** $\Delta T_{\text{strip}} < 0$ (sharp, repeatable endothermic cooling proportional to tunnel-ionized feed rate).

---

## 6. Repository Layout & Dual Reciprocal Copyleft Licensing

```text
Caloricum/
├── caloricum/
│   ├── __init__.py                         # Importable package interface (used by Prometheus)
│   └── core.py                             # Standoff, Larmor, cryo-TPV, C-C & mass-ledger physics core
├── docs/
│   └── BENCHTOP_FALSIFICATION_PROTOCOL.md  # University/garage bell-jar kill-test specification
├── scripts/
│   └── caloricum_sizing_audit.py           # Standalone verification & sizing audit (exit 0)
├── DEFENSIVE_PRIOR_ART.md                  # Statutory anti-enclosure disclosure (DOI: 10.5281/zenodo.24281039)
├── LICENSE-AGPLv3.txt                      # GNU AGPLv3 (all software, simulation & pulse-control code)
├── LICENSE-CERN-OHL-S-v2.txt               # CERN-OHL-S v2 (all hardware geometries, manifolds & optics)
└── README.md
```

- **Software, Simulation & Pulse-Control Code:** Licensed under the **GNU Affero General Public License v3.0** ([`LICENSE-AGPLv3.txt`](./LICENSE-AGPLv3.txt)).
- **Physical Hardware Geometries, Manifolds & Optical Layouts:** Licensed under the **CERN Open Hardware Licence Version 2 - Strongly Reciprocal** ([`LICENSE-CERN-OHL-S-v2.txt`](./LICENSE-CERN-OHL-S-v2.txt)).
- **Anti-Enclosure Prior Art:** See [`DEFENSIVE_PRIOR_ART.md`](./DEFENSIVE_PRIOR_ART.md) (anchored to Phase Wave Cosmology master DOI [`10.5281/zenodo.24281039`](https://doi.org/10.5281/zenodo.24281039)).
