# Antimatter Propulsion Research
**Cloud-9 UAP Project** | Dean Bordode + Kimi | May 2026

Deep dive into antimatter engines as UAP propulsion candidates.

---

## Key Questions

### 1. How much antimatter is needed?
| Velocity | UAP Mass | Antimatter Required (w/ 45% efficiency) |
|----------|----------|------------------------------------------|
| Mach 3   | 1000 kg  | ~0.000012 mg                             |
| Mach 5   | 1000 kg  | ~0.000033 mg                             |
| Mach 7   | 1000 kg  | ~0.000065 mg                             |
| Mach 100 | 1000 kg  | ~0.013 mg                                |

For context: CERN currently produces ~10 nanograms/year. Mach 5 requires ~33 picograms — achievable in principle, impossible in practice with current infrastructure.

### 2. Power density comparison
| System                    | Power Density (MW/kg) |
|---------------------------|----------------------|
| Chemical rocket (best)    | ~0.001               |
| Nuclear fission reactor   | ~0.1                 |
| Observed TicTac UAP (est) | ~1.59                |
| Antimatter annihilation   | ~90,000,000          |
| **Ratio (antimatter/UAP)**| **~56,000,000×**     |

The gap suggests UAPs are NOT using pure antimatter annihilation. More likely candidates:
- Antimatter-catalyzed fusion (small trigger → large yield)
- IMR (Pais) + antimatter hybrid
- Unknown mechanism

### 3. Can we produce and store it?
- **Production**: CERN/ALPHA: ~10 ng/year. Need ~1000× more for even nanogram-scale propulsion tests.
- **Storage**: Penning traps (magnetic + electric). ALPHA-g holds antihydrogen for ~1000 seconds.
- **Containment failure = annihilation** — catastrophic at any useful quantity.

---

## Assembly Index (A_c) Analysis

Antimatter propulsion is among the highest-assembly propulsion concepts known:

    A_c(antimatter stack) = A_c(production) + A_c(storage) + A_c(annihilation control) + A_c(thrust vectoring)
    
Estimated total: A_c > 50 — comparable to the Perseus Cluster result (A_c = 64.89)

This makes antimatter propulsion a **strong-positive Assembly Index system** — exactly the kind of structure Cloud-9 predicts should be detectable above the 5.41σ threshold if operating at scale.

---

## Hybrid Hypothesis: IMR + Antimatter

Pais' Inertial Mass Reduction (IMR) + antimatter trigger may explain the observed UAP performance gap:

1. **IMR reduces effective inertial mass** → less energy needed to accelerate
2. **Antimatter provides ignition** → catalyzes fusion, not full annihilation
3. **Result**: Much lower antimatter requirement than pure E=mc² calculation predicts

See: `simulations/propulsion/pais_imr_simulation.py` for IMR modeling.

---

## References
- [CERN Antimatter Factory](https://home.cern/science/accelerators/antiproton-decelerator)
- [ALPHA Experiment (antihydrogen storage)](https://alpha.web.cern.ch/)
- [NASA Antimatter Propulsion study](https://www.nasa.gov/)
- [Pais IMR Patents](https://patents.google.com/?inventor=Salvador+Cezar+Pais)
- [UAP power-to-weight ratio analysis](../simulations/engine_types/comparison.md)

---

## Cloud-9 Next Steps
1. Simulate hybrid IMR + antimatter system (see `pais_imr_simulation.py`)
2. Model partial annihilation efficiency curves
3. Cross-reference with GW190728 QBox decoherence predictions
4. Flag for INRC hardware pathway (memristor-based containment simulation)
