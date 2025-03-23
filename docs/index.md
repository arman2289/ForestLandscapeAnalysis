# Forest Landscape Analysis Documentation

Welcome to the documentation for the Forest Landscape Analysis package.

## Introduction

This package provides tools for analyzing forest landscape dynamics and fragmentation using remote sensing data. The methodologies implemented are based on research studies of the Western Ghats in India, a biodiversity hotspot experiencing significant forest changes.

## Research Applications

The tools provided by this package can be used for:

- Land use change analysis: Track changes in forest cover over time
- Fragmentation quantification: Classify forest into interior, edge, perforated, etc.
- Spatial metrics computation: Calculate metrics to characterize landscape patterns
- Visualization: Create informative plots and maps of forest changes
- Conservation planning: Identify priority areas for conservation efforts


## Installation

```bash
pip install git+https://github.com/yourusername/ForestLandscapeAnalysis.git
example python
from forestlandscape.core.land_use_analysis import LandUseAnalysis
from forestlandscape.visualization.landuse_plots import LandUsePlotter

# Create an analyzer instance
analyzer = LandUseAnalysis()

# Calculate change rate for evergreen forest cover
change_rate = analyzer.calculate_change_rate(
    area_t0=67.73,  # Evergreen forest cover in 1973 (%)
    area_t1=29.5,   # Evergreen forest cover in 2016 (%)
    time_diff=43    # Time difference in years
)
print(f"Annual change rate: {change_rate:.2f}% per year")
