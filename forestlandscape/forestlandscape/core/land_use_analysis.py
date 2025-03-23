# forestlandscape/core/land_use_analysis.py
import numpy as np
import pandas as pd

class LandUseAnalysis:
    """
    Class for analyzing land use changes from remote sensing data.
    
    This implements methods for:
    - Calculating vegetation indices (NDVI)
    - Computing land use change statistics
    - Analyzing temporal patterns in land cover
    """
    
    def __init__(self):
        """Initialize the LandUseAnalysis class."""
        self.data = None
        
    def calculate_ndvi(self, red_band, nir_band):
        """
        Calculate Normalized Difference Vegetation Index.
        
        NDVI = (NIR - Red) / (NIR + Red)
        
        Parameters:
        -----------
        red_band : numpy.ndarray
            Red band values
        nir_band : numpy.ndarray
            Near Infrared band values
            
        Returns:
        --------
        numpy.ndarray
            NDVI values ranging from -1 to 1
        """
        # Avoid division by zero
        denominator = nir_band + red_band
        ndvi = np.where(
            denominator > 0,
            (nir_band - red_band) / denominator,
            0
        )
        return ndvi
        
    def calculate_change_rate(self, area_t0, area_t1, time_diff):
        """
        Calculate annual rate of land use change.
        
        rate = (ln(A_t1) - ln(A_t0)) / (t1 - t0) * 100
        
        Parameters:
        -----------
        area_t0 : float
            Area at time t0
        area_t1 : float
            Area at time t1
        time_diff : float
            Time difference in years
            
        Returns:
        --------
        float
            Annual rate of change in percentage
        """
        return (np.log(area_t1) - np.log(area_t0)) / time_diff * 100
