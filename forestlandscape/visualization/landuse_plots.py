# forestlandscape/visualization/landuse_plots.py
import matplotlib.pyplot as plt
import numpy as np

class LandUsePlotter:
    """
    Class for creating visualizations of land use data and changes.
    """
    
    def __init__(self, style='default'):
        """
        Initialize with matplotlib style.
        
        Parameters:
        -----------
        style : str
            Matplotlib style to use
        """
        plt.style.use(style)
        
    def plot_vegetation_cover_change(self, years, vegetation_percentages, 
                                    non_vegetation_percentages=None, 
                                    title="Vegetation Cover Change", 
                                    figsize=(10, 6)):
        """
        Plot vegetation cover change over time.
        
        Parameters:
        -----------
        years : list or array
            Years for which data is available
        vegetation_percentages : list or array
            Percentage of vegetation cover for each year
        non_vegetation_percentages : list or array, optional
            Percentage of non-vegetation cover for each year
        title : str
            Title for the plot
        figsize : tuple
            Figure size (width, height)
            
        Returns:
        --------
        matplotlib.figure.Figure
            The created figure
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        ax.plot(years, vegetation_percentages, 'o-', color='forestgreen', 
               linewidth=2.5, label='Vegetation')
        
        if non_vegetation_percentages is not None:
            ax.plot(years, non_vegetation_percentages, 'o-', color='indianred', 
                   linewidth=2.5, label='Non-Vegetation')
        
        ax.set_title(title, fontsize=15)
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Percentage (%)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(fontsize=12)
        
        plt.tight_layout()
        return fig
        
    def plot_fragmentation_summary(self, years, interior_percentages, edge_percentages,
                                 patch_percentages, transitional_percentages,
                                 perforated_percentages, title="Forest Fragmentation Trends",
                                 figsize=(12, 6)):
        """
        Plot forest fragmentation trends over time.
        
        Parameters:
        -----------
        years : list or array
            Years for which data is available
        interior_percentages : list or array
            Percentage of interior forest for each year
        edge_percentages : list or array
            Percentage of edge forest for each year
        patch_percentages : list or array
            Percentage of patch forest for each year
        transitional_percentages : list or array
            Percentage of transitional forest for each year
        perforated_percentages : list or array
            Percentage of perforated forest for each year
        title : str
            Title for the plot
        figsize : tuple
            Figure size (width, height)
            
        Returns:
        --------
        matplotlib.figure.Figure
            The created figure
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        ax.plot(years, interior_percentages, 'o-', color='darkgreen', 
               linewidth=2.5, label='Interior')
        ax.plot(years, edge_percentages, 'o-', color='forestgreen', 
               linewidth=2.5, label='Edge')
        ax.plot(years, perforated_percentages, 'o-', color='limegreen', 
               linewidth=2.5, label='Perforated')
        ax.plot(years, transitional_percentages, 'o-', color='gold', 
               linewidth=2.5, label='Transitional')
        ax.plot(years, patch_percentages, 'o-', color='orangered', 
               linewidth=2.5, label='Patch')
        
        ax.set_title(title, fontsize=15)
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Percentage (%)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(fontsize=12)
        
        plt.tight_layout()
        return fig
