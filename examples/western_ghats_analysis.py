# examples/western_ghats_analysis.py
"""
Example script demonstrating the analysis of forest landscape dynamics 
in the Western Ghats region of India.
"""

from forestlandscape.core.land_use_analysis import LandUseAnalysis
from forestlandscape.visualization.landuse_plots import LandUsePlotter
import matplotlib.pyplot as plt

def main():
    """Run the Western Ghats forest landscape analysis example."""
    # Initialize analyzer and plotter
    analyzer = LandUseAnalysis()
    plotter = LandUsePlotter()
    
    # Western Ghats vegetation cover data (1973-2016)
    years = [1973, 1979, 1989, 1999, 2010, 2013, 2016]
    vegetation_cover = [92.87, 89.25, 86.36, 83.72, 82.14, 81.05, 80.42]
    non_vegetation_cover = [7.13, 10.75, 13.64, 16.28, 17.86, 18.95, 19.58]
    
    # Plot vegetation cover change
    fig1 = plotter.plot_vegetation_cover_change(
        years, 
        vegetation_cover, 
        non_vegetation_cover,
        title="Vegetation Cover Change in Western Ghats (1973-2016)"
    )
    
    # Calculate annual change rate for vegetation cover
    period_years = years[-1] - years[0]
    change_rate = analyzer.calculate_change_rate(
        vegetation_cover[0], 
        vegetation_cover[-1], 
        period_years
    )
    print(f"Annual vegetation loss rate: {abs(change_rate):.2f}% per year")
    
    # Western Ghats forest fragmentation data (1979-2013)
    frag_years = [1979, 1989, 1999, 2013]
    interior_forest = [64.42, 53.33, 40.74, 25.62]
    edge_forest = [7.32, 12.00, 16.35, 17.48]
    perforated_forest = [1.80, 1.38, 1.11, 0.87]
    transitional_forest = [1.98, 3.29, 3.97, 5.78]
    patch_forest = [0.36, 1.30, 1.75, 2.98]
    
    # Plot fragmentation trends
    fig2 = plotter.plot_fragmentation_summary(
        frag_years,
        interior_forest,
        edge_forest,
        patch_forest,
        transitional_forest,
        perforated_forest,
        title="Forest Fragmentation Trends in Western Ghats (1979-2013)"
    )
    
    # Display the plots
    plt.show()

if __name__ == "__main__":
    main()
