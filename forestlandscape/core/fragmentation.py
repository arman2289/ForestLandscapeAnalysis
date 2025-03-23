# forestlandscape/core/fragmentation.py
import numpy as np

class ForestFragmentation:
    """
    Class for analyzing forest fragmentation based on the methodology of 
    Riitters et al. (2002).
    
    Implements methods for:
    - Computing Pf (proportion of forest pixels)
    - Computing Pff (proportion of forest-forest adjacencies)
    - Classifying fragmentation into interior, edge, perforated, etc.
    """
    
    CATEGORIES = {
        'interior': 0,
        'perforated': 1,
        'edge': 2,
        'transitional': 3,
        'patch': 4,
        'non_forest': 5
    }
    
    def __init__(self, forest_mask=None):
        """
        Initialize the ForestFragmentation class.
        
        Parameters:
        -----------
        forest_mask : numpy.ndarray, optional
            Binary mask where 1 = forest, 0 = non-forest
        """
        self.forest_mask = forest_mask
        self.pf = None
        self.pff = None
        self.fragmentation_map = None
        
    def set_forest_mask(self, forest_mask):
        """
        Set or update the forest mask.
        
        Parameters:
        -----------
        forest_mask : numpy.ndarray
            Binary mask where 1 = forest, 0 = non-forest
        """
        self.forest_mask = forest_mask
        # Reset computed values
        self.pf = None
        self.pff = None
        self.fragmentation_map = None
        
    def get_fragmentation_stats(self):
        """
        Get statistics about fragmentation categories.
        
        Returns:
        --------
        dict
            Dictionary with percentage of each fragmentation category
        """
        if self.fragmentation_map is None:
            self.classify_fragmentation()
            
        total_pixels = self.fragmentation_map.size
        stats = {}
        
        for category, value in self.CATEGORIES.items():
            pixels = np.sum(self.fragmentation_map == value)
            percentage = (pixels / total_pixels) * 100
            stats[category] = percentage
            
        return stats
