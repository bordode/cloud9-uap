# 📊 UAP Engine Comparison
**Side-by-side analysis of propulsion systems vs. observed UAP performance.**

## Performance Targets (from declassified data)
- Acceleration: **500+ Gs** (TicTac Nimitz)
- Power density: **~1.59 MW/kg** (Fravor estimates)
- Velocity: **Mach 5+**
- Special: No sonic boom, transmedium capable

## Comparison Table

| Engine Type | Power Density (MW/kg) | Max Accel (Gs) | Max Velocity | Feasibility | C9 Priority |
|-------------|----------------------|----------------|--------------|-------------|-------------|
| Chemical Rockets | 0.01 | 10 | Mach 5 | ✅ Proven | ❌ Low |
| Nuclear Thermal | 0.1 | 20 | Mach 10 | ✅ Tested | ❌ Low |
| Ion Thrusters | 0.001 | 0.1 | Mach 0.1 | ✅ Operational | ⚠️ Medium |
| **Antimatter Fusion** | **1000+** | **1000+** | **Mach 100+** | ⚠️ Low-term | 🟢 **High** |
| **Inertial Mass Reduction** | N/A (reduces mass) | **500+** | **Mach 5+** | ⚠️ Medium | 🟢 **High** |
| **IMR + Antimatter Hybrid** | **1000+** | **1000+** | **Mach 100+** | ⚠️ Medium | 🟢 **Highest** |
| Alcubierre Warp Drive | N/A (warps spacetime) | N/A | FTL | ❌ Theoretical | ⚠️ Medium |
| Quantum Vacuum Thruster | 0.1–1.0 | 1–10 | Mach 1–10 | ⚠️ Experimental | ⚠️ Medium |

## 🔬 Assembly Index (A_c) Connection

| Engine | Hybridization Depth | Estimated A_c | Notes |
|--------|-------------------|--------------|-------|
| Chemical | Low (1 reaction type) | ~5 | Single chemistry |
| Nuclear Thermal | Medium (fission + thrust) | ~15 | Two coupled systems |
| IMR | High (EM + inertia + vacuum) | ~30-50 | Triple coupling |
| Antimatter | Very High (matter/antimatter + GW) | ~80-200 | Mirrors GW190728 system |
| IMR + Antimatter Hybrid | Extreme | ~200+ | Maximum hybridization |

> **Key insight from C9-2026-PHY-001**: A_c scales superlinearly with hybridization depth.
> The IMR + Antimatter hybrid is the highest-A_c propulsion concept — matching the
> GW190728 dark matter system's energy scale bridging (79 orders of magnitude).

## 🎯 Cloud 9 Focus: Hybrid IMR + Antimatter
1. **Phase 1**: Prototype small EM coils for IMR simulation (`hardware/`)
2. **Phase 2**: Simulate hybrid engine in Python (`imr_engine.ipynb`)
3. **Phase 3**: CERN collaboration for antimatter data
4. **Phase 4**: Scale validation against PURSUE declassified flight data
