# Cloud-9 Assembly: UAP Analysis Pipeline (DOW-UAP-PR38)

**Status**: Open for Collaboration  
**License**: MIT  
**Last Updated**: June 18, 2026

## Project Overview

Reproducible, open-source pipeline for analyzing the 2013 UAP video (DOW-UAP-PR38) using computer vision, signal processing, and optical flow techniques.

**Key Features**:
- Empirical Layer: Frame-by-frame analysis (contours, optical flow, FFT)
- Modular Design: Separate scripts for each analytical step
- Collaborative: Designed for cross-validation with other researchers

## Empirical Findings

### Video Properties
| Metric | Value | Notes |
|--------|-------|-------|
| Source | DOW-UAP-PR38 | 2013 Middle East, infrared footage |
| Resolution | 1078×842 pixels | From metadata |
| FPS | 36.39 | From metadata |
| Total Frames | 3,954 | Full video length |
| Peak Window | Frames 163–454 (4.5–12.5 sec) | Highest motion activity |

### Motion Anomalies
| Metric | Value | Interpretation |
|--------|-------|----------------|
| Max Frame-Difference | 223.02 px/frame (Frame 204) | Peak motion signal in ROI |
| 99th Percentile Frame-Difference | 41.324 px/frame | Extreme motion burst |
| Median Optical Flow | 0.00187 px/frame | Baseline movement |
| Acceleration Anomalies | 38 frames (avg: 38.77 px/frame², max: 479.42) | Non-linear motion |

### Geometry & Shape Analysis
| Metric | Value | Interpretation |
|--------|-------|----------------|
| Most Common Vertices | 5 | Unstable contours |
| Golden Ratio Match | 3 frames (37, 38, 39) | Side ratios ≈ 1.618 (within 1%) |
| 8-Pointed Star | 0 frames | Not detected (current parameters) |

### Harmonic Resonance (Brightness FFT)
| Metric | Value | Interpretation |
|--------|-------|----------------|
| Dominant Frequency | 0.997 Hz | Time-series feature only |

## Pipeline Structure

```
uap_analysis/
├── data/
│   ├── raw/                    # Original video
│   ├── frames/                 # Extracted frames (163-454)
│   └── cropped/                # ROI-cropped frames
├── results/
│   ├── empirical/              # CSV metrics
│   └── visualizations/         # Plots, contact sheets
├── scripts/
│   ├── 01_extract_frames.py
│   ├── 02_optical_flow.py
│   ├── 03_contour_analysis.py
│   ├── 04_brightness_fft.py
│   └── 05_visualize_results.py
└── requirements.txt
```

## Dependencies

```
opencv-python>=4.5.0
numpy>=1.20.0
matplotlib>=3.4.0
scipy>=1.7.0
pandas>=1.3.0
scikit-image>=0.18.0
```

## Quick Start

```bash
git clone https://github.com/bordode/cloud9-uap.git
cd cloud9-uap
pip install -r requirements.txt
python scripts/01_extract_frames.py
python scripts/02_optical_flow.py
python scripts/03_contour_analysis.py
python scripts/04_brightness_fft.py
python scripts/05_visualize_results.py
```

## Results Summary

| Category | Finding | Confidence | Next Steps |
|----------|---------|------------|------------|
| Motion Anomalies | 38 frames high acceleration | High | Validate with raw sensor data |
| Golden Ratio | 3 frames (37-39), ratios ≈ 1.618 | Medium | Refinement needed |
| Harmonic Resonance | 0.997 Hz dominant | None | Denoise + re-run FFT |

## Collaboration

Open invitation to:
- Scientists: Validate the empirical layer
- Researchers: Test hypotheses with better data
- Developers: Improve the pipeline

**Cross-validation targets**: Avi Loeb's UAP Science Advisory Council, AARO

## Citation

```
@misc{cloud9_uap_analysis,
  author = {Dean Bordode},
  title = {Cloud-9 Assembly: UAP Analysis Pipeline (DOW-UAP-PR38)},
  year = {2026},
  url = {https://github.com/bordode/cloud9-uap}
}
```

## License

MIT License — see LICENSE file for details.
