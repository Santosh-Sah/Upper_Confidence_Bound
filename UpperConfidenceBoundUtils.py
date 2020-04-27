# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:19:08 2020

@author: Santosh Sah
"""

"""
importing the libraries
"""

import pandas as pd

# Importing the dataset
def importUpperConfidenceBoundDataset(upperConfidenceBoundDatasetFileName):
    
    # Importing the dataset
    upperConfidenceBoundDataset = pd.read_csv(upperConfidenceBoundDatasetFileName)
    
    return upperConfidenceBoundDataset
    