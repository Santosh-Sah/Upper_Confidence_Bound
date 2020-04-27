# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:21:10 2020

@author: Santosh Sah
"""

import pandas as pd
import matplotlib.pyplot as plt
from UpperConfidenceBoundUtils import (importUpperConfidenceBoundDataset)
"""
Visualizing UpperConfidenceBound result
"""
def visualisingUpperConfidenceBoundtResult():
    print("santosh")
    upperConfidenceBoundResult = pd.read_csv("advertisementsSelected.csv")
    
    plt.hist(upperConfidenceBoundResult.values)
    plt.title('Histogram of the advertisement selected')
    plt.xlabel('Advertisement')
    plt.ylabel('Number of times each advertisement was selected')
    
    plt.savefig("Upper_Confidence_Bound_result.png")
    
    plt.show()

if __name__ == "__main__":
    visualisingUpperConfidenceBoundtResult()