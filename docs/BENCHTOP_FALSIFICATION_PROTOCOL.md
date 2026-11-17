# Benchtop Falsification Protocol: Vacuum Bell-Jar Endothermic Kill-Test

- **Repository:** `Caloricum` ([`https://github.com/fringeneering-jpg/Caloricum`](https://github.com/fringeneering-jpg/Caloricum))
- **Theoretical Anchor:** Phase Wave Cosmology ([DOI: `10.5281/zenodo.24281039`](https://doi.org/10.5281/zenodo.24281039))
- **Hardware License:** CERN-OHL-S v2 ([`../LICENSE-CERN-OHL-S-v2.txt`](../LICENSE-CERN-OHL-S-v2.txt))

---

## 1. Objective & Binary Kill Criterion

This document specifies a low-cost, decisive **falsification experiment** executable in any university ultrafast optics teaching lab or well-equipped garage vacuum setup using off-the-shelf components. It directly tests whether transverse **cold femtosecond tunnel ionization** ($\tau_p \le 100\text{ fs}$, $I = 10^{15}\text{–}10^{16}\text{ W/cm}^2$, Keldysh $\gamma_K \ll 1$) of a dense tungsten (`W`) wire across an evacuated gap produces net **endothermic cooling** of an adjacent pyrolytic Carbon-Carbon (`C-C`) witness strip shielded by a parallel $0.5\text{ T}$ magnetic ion curtain:

| Framework | Physical Mechanism | Predicted Witness-Strip Temperature Shift ($\Delta T_{\text{strip}}$) |
| :--- | :--- | :--- |
| **Classical Plasma / MHD / Radiative Transfer** | Laser pulse Energy $E_p$ partitions strictly into electron/ion kinetic energy, scattered photons, and bremsstrahlung/recombination UV emission ($Q_{\text{rad}} > 0$). With vacuum convection negligible at $0.1\text{–}10\text{ mTorr}$ and ions magnetically deflected, energy transfer to the witness strip is strictly **positive or zero**. | **$\Delta T_{\text{strip}} \ge 0\text{ K}$** *(Monotonic radiative warming)* |
| **Phase Wave Cosmology (`Caloricum` Untying)** | Sub-$100\text{ fs}$ tunnel stripping ($\tau_p \ll \tau_{\text{e-ph}}$) unbinds nuclear knots before lattice thermalization, generating an acute local continuum decompression trough ($q_{\text{eff}} \sim 2.5 \times 10^{17}\text{ J/kg}$ ideal limit; measurable even at $10^{-9}\text{–}10^{-6}$ fractional coupling on a micro-joule/milli-joule tabletop rig) that extracts phonon energy across the $2\text{–}5\text{ cm}$ standoff gap. | **$\Delta T_{\text{strip}} < 0\text{ K}$** *(Prompt, repeatable endothermic temperature drop below radiative equilibrium)* |

**Hard Falsification Rule:** If, across verified tunneling intensities ($10^{15}\text{–}10^{16}\text{ W/cm}^2$, $\tau_p \le 100\text{ fs}$), vacuum pressures ($0.1\text{–}10\text{ mTorr}$), and standoffs ($2\text{–}5\text{ cm}$) with zero ion impingement confirmed on the witness strip, the strip exhibits only $\Delta T_{\text{strip}} \ge 0\text{ K}$ within calibrated sensor noise ($\pm 0.02\text{ K}$), the `Caloricum` endothermic untying hypothesis is **falsified** in that operating regime. Conversely, any reproducible $\Delta T_{\text{strip}} < -0.20\text{ K}$ (> $10\sigma$ below the adiabatic/radiative baseline while continuous resistive bias $P_{\text{bias}}$ is held constant) violates classical passive vacuum heat transfer and confirms continuum endothermic wicking.

---

## 2. Apparatus & Bill of Materials (Standard Lab / Garage Scale)

```text
          Vacuum Bell Jar / 6-Way KF-40 or ISO-160 Cross (0.1 - 10 mTorr)
   +-------------------------------------------------------------------------+
   |                                                                         |
   |   [DC Bias Leads]               [Type-E/K Shielded Thermocouples x3]    |
   |         |                                      |                        |
   |   ======+======================================+======   Ceramic Mounts  |
   |   [     2-3 mm Pyrolytic C-C Witness Strip (Pre-heated 350-500 K)    ]  |
   |   --------------------------------------------------------------------  |
   |   [  15 um W Foil Backstop (Grounded Faraday / Optical Shield on Back) ]|
   |                                                                         |
   |     =========  B = 0.5 T Parallel NdFeB / SmCo Yoke (B || Strip) =====  |
   |                         ^                                               |
   |                         |  Standoff d = 2.0 to 5.0 cm (Micrometer Stage)|
   |                         v                                               |
   |   (o) <--- 10-25 um Spooled W Wire (Stepper Feed: 0.1 - 5 mm/s)         |
   |    *  <--- Transverse Femtosecond Focus (tau_p <= 100 fs, 1 kHz,        |
   |            w_0 ~ 3-5 um, I_peak ~ 10^15 - 10^16 W/cm^2, beam || strip)  |
   |                                                                         |
   +------------------------------------+------------------------------------+
                                        |
                         [Optical Beam Dump + Power Meter]
```

1. **Vacuum Chamber & Pumping (`$800–$3,500` surplus/new):**
   - Borosilicate bell jar on aluminum baseplate or stainless 6-way `ISO-160` / `CF-6"` chamber with fused-silica (`UVFS`, $t \le 3\text{ mm}$ low-GVD) entrance/exit windows.
   - Two-stage rotary vane or scroll roughing pump + small turbomolecular or diffusion pump maintaining **$0.1\text{–}10\text{ mTorr}$** ($0.013\text{–}1.33\text{ Pa}$), monitored by Pirani/capacitance manometer. *(At $1\text{ mTorr}$, gas mean free path $\lambda_{\text{mfp}} \approx 5\text{ cm} \ge d$, suppressing residual gas conduction.)*
2. **Ultrafast Laser Source (Existing University kHz Amplifier or Rental Fiber/Ti:Sa):**
   - Wavelength $\lambda = 800\text{ nm}$ (Ti:Sapphire) or $1,030\text{ nm}$ (Yb-doped chirped-pulse amplifier).
   - Pulse width $\tau_p \le 100\text{ fs}$ (verified at target plane via FROG/autocorrelator after window pre-chirp compensation).
   - Pulse energy $E_p = 0.5\text{–}5.0\text{ mJ}$ at $f_{\text{rep}} = 1\text{ kHz}$ ($0.5\text{–}5.0\text{ W}$ average beam power), focused by an off-axis parabolic mirror ($f = 100\text{–}150\text{ mm}$) to spot radius $w_0 \approx 3.0\text{–}5.0\text{ }\mu\text{m}$:
     $$I_{\text{peak}} = \frac{2 E_p}{\pi w_0^2 \tau_p} \approx 1.3 \times 10^{15}\text{ to } 1.4 \times 10^{16}\text{ W/cm}^2$$
   - Beam propagates **strictly parallel** to the `C-C` witness strip face and exits into a blackened Brewster cone beam dump outside the exit window so zero primary laser light strikes the strip.
3. **Sacrificial Feed Assembly:**
   - $10\text{–}25\text{ }\mu\text{m}$ diameter high-purity ($99.95\%$) drawn tungsten (`W`) wire fed continuously from pay-out spool to take-up / pinch-roller drive at $0.1\text{–}5.0\text{ mm/s}$ across the focal waist.
4. **Parallel Magnetic Ion-Deflection Curtain ($B = 0.5\text{ T}$):**
   - Dual Sintered `SmCo` (high-$T$ rated to $300^\circ\text{C}$) or water/heatsink-mounted `N52 NdFeB` bar magnets on a soft-iron C-yoke producing a uniform **$B = 0.50 \pm 0.05\text{ T}$** field parallel to the `C-C` strip across the $2\text{–}5\text{ cm}$ gap (verified by Hall probe).
   - Confines epithermal & multiply ionized $\text{W}^{Z+}$ ions to $r_L \approx 3\text{–}11\text{ mm} < d$.
5. **Heated `C-C` Witness Strip & Differential Thermometry:**
   - Dimensions: $50\text{ mm} \times 10\text{ mm} \times 2.5\text{ mm}$ 3D pyrolytic Carbon-Carbon (`C-C`) or high-purity pyrolytic graphite strip suspended on low-conductivity macor/alumina knife-edge standoffs.
   - Pre-heated to steady radiative equilibrium **$T_0 = 400.0\text{ K}$** (or cryo-cooled test point at $77\text{ K}$ via $\text{LN}_2$ cold-finger strap with heater trim) using a precision constant-power 4-wire DC current source ($\pm 0.01\%$ regulation).
   - **Primary readout:** Three mineral-insulated, grounded-sheath Faraday-screened `Type E` (chromel–constantan, non-magnetic, $68\text{ }\mu\text{V/K}$) thermocouples bonded to the rear face behind a grounded $15\text{ }\mu\text{m}$ `W` foil EMI shield, logged at $100\text{ Hz}$ via a 24-bit isolated DAQ.
   - **Independent optical cross-check:** External `8–14 um` Ge-windowed thermal IR camera / two-color pyrometer viewing the rear blackened patch of the `C-C` strip (completely immune to electrical/EMP pickup).

---

## 3. Step-by-Step Experimental & Control Matrix

To eliminate every classical artifact (EMI pickup on thermocouples, conductive gas cooling, desorption cooling, heater power drift, or ion sputtering), run the following **five-stage locked sequence** at fixed standoff $d = 3.0\text{ cm}$ and chamber pressure $p = 1.0\text{ mTorr}$:

| Run ID | Configuration | Purpose | Expected Classical Result | Expected `Caloricum` Result |
| :--- | :--- | :--- | :--- | :--- |
| **C-0 (Baseline)** | DC bias ON ($T_0 = 400.00\text{ K}$ steady for $600\text{ s}$), Laser OFF, Wire feed ON | Establish thermal drift floor & mechanical feed vibration noise | $|\Delta T| < 0.02\text{ K}$ | $|\Delta T| < 0.02\text{ K}$ |
| **C-1 (Laser-Only Blank)** | Laser ON ($100\text{ fs}$, $1\text{ kHz}$), Wire retracted out of beam | Quantify stray window scatter + EMP/RF noise on thermocouples vs. IR pyrometer | $\Delta T \approx 0.00\text{ to }+0.05\text{ K}$ | $\Delta T \approx 0.00\text{ to }+0.05\text{ K}$ |
| **C-2 (Stretched Pulse Thermal Control)** | Grating compressor detuned to **$\tau_p = 50\text{ ps}\text{–}1\text{ ns}$** ($I \sim 10^{11}\text{–}10^{12}\text{ W/cm}^2$, $\gamma_K > 1$, classical thermal plasma), Wire IN | Prove classical hot ablation/bremsstrahlung **heats** the strip when pulse exceeds $\tau_{\text{e-ph}}$ | **$\Delta T > +0.3\text{ K}$** (radiative plasma heating) | **$\Delta T > +0.3\text{ K}$** (no cold tunnel untying when $\tau_p \gg \tau_{\text{e-ph}}$) |
| **T-1 (Active Tunnel-Untying Kill-Test)** | Compressor locked at **$\tau_p \le 100\text{ fs}$** ($I = 3 \times 10^{15}\text{ W/cm}^2$, $\gamma_K \ll 1$), Wire IN, $B = 0.5\text{ T}$ ON, $60\text{ s}$ burst | **Primary Kill-Test** | **$\Delta T \ge 0\text{ K}$** | **$\Delta T < -0.5\text{ K}$ to $-15\text{ K}$** *(thermocouple AND IR pyrometer drop in unison)* |
| **T-2 (Standoff & Pressure Sweep)** | Repeat **T-1** at $d \in \{2.0, 3.0, 5.0, 8.0, 12.0\}\text{ cm}$ and $p \in \{0.1, 1.0, 10.0\}\text{ mTorr}$ | Verify $d_{\min}\text{–}d_{\max}$ reach curve & pressure independence across molecular-flow regime | $\Delta T \ge 0\text{ K}$ at all $(d, p)$ | Cooling peak inside $2\text{–}5\text{ cm}$, tapering smoothly past $d_{\max} \sim 8\text{–}10\text{ cm}$ |

---

## 4. Post-Run Witness Inspection & Calorimetric Extraction

1. **Zero-Sputtering Verification:** Place a clean quartz crystal microbalance (QCM) wafer or Si witness coupon flush with the `C-C` strip face during **T-1**. Confirm via optical profilometry / EDX that tungsten deposition with the $0.5\text{ T}$ magnetic curtain active is statistically indistinguishable from background ($< 1\text{ \AA}$ after $10^5$ shots), proving $r_L < d$.
2. **Calorimetric Power Extraction ($\dot{Q}_{\text{wick}}$):** For strip mass $m_s \approx 2.75\text{ g}$ ($\rho_{\text{C-C}} \approx 2,200\text{ kg/m}^3$, $c_p(400\text{ K}) \approx 950\text{ J/(kg}\cdot\text{K)}$, heat capacity $C_s \approx 2.61\text{ J/K}$), measure both the initial cooling slope $\dot{Q}_{\text{wick}} = -C_s (dT/dt)_{t=0^+}$ and the additional DC electrical trim power $\Delta P_{\text{DC}}$ required to null $\Delta T_{\text{strip}} \to 0.00\text{ K}$ (isothermal power-substitution calorimetry, eliminating emissivity assumptions).
3. **Open Publication of Raw Traces:** Publish raw $100\text{ Hz}$ thermocouple CSV logs, IR thermograms, FROG pulse traces, and QCM deposition checks openly under `CC BY-SA 4.0` / `CERN-OHL-S-2.0`.
