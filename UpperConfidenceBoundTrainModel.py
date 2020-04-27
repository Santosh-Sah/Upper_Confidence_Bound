# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:20:52 2020

@author: Santosh Sah
"""

import math
import pandas as pd
from UpperConfidenceBoundUtils import (importUpperConfidenceBoundDataset)

#train UpperConfidenceBound model
def trainUpperConfidenceBound():
    
    upperConfidenceBoundDataset = importUpperConfidenceBoundDataset("Ads_CTR_Optimisation.csv")
    
    #number of times the different advertisement shown to the users on the social media.
    N = 10000
    
    #number of version of the advertisement
    d = 10
    
    #different versions of advertisements selected
    advertisementsSelected = []
    
    #there are three steps present in the training of trainUpperConfidenceBound.
    #We are creating a model which used to select the best advertisement of a company.
    #step 1
    #at each round of n we consider two number for each ad i.
    #first is the number of times the ad i was selected up to round n
    #second is sum of rewards of the ad i up to round n
    numberOfSelections = [0] * d
    sumOfRewards = [0] * d
    totalRewards = 0
    
    #step 2
    #from these two numbers we compute two things.
    #the average of rewards of ad i up to round n
    #confidence interval at round n
    for n in range(0, N):
        
        advertisementWithMaxUpperBound = 0
        
        maximumUpperBound = 0
        
        for i in range(0, d):
            
            #choose the advertisement at first 10 round. initially we do not have any information about all these things.
            #we need to select advertisement in first 10 round without any strategy. We have define the startegy here 
            #but we will implement these strategy after 10 rounds when we have some information available.
            #for first 10 round what we will do at round 1 select advertisment 1 and up to round 10 select ad 10.
            if numberOfSelections[i] > 0:
                
                averageReward = sumOfRewards[i] / numberOfSelections[i]
                
                delta_i = math.sqrt(3/2 * math.log(n + 1) / numberOfSelections[i])
                
                upperBound = averageReward + delta_i
            
            else:
                
                #whey we are assigned upper bound such a huge number. for the first round 0 we will go the 10 version of the ad.
                #for the first 10 round no ad will be selected. It will make sure that the first 10 round respective 10 ad will be selected.
                upperBound = 1e400
            
            #step 3
            #select the ad i that has the maximum upper confidence bound
            if upperBound > maximumUpperBound:
                
                maximumUpperBound = upperBound
                
                advertisementWithMaxUpperBound = i
        
        advertisementsSelected.append(advertisementWithMaxUpperBound)
        
        #update numberOfSelections
        numberOfSelections[advertisementWithMaxUpperBound]  = numberOfSelections[advertisementWithMaxUpperBound] + 1
        
        #update sumOfRewards
        rewards = upperConfidenceBoundDataset.values[n, advertisementWithMaxUpperBound]
        sumOfRewards[advertisementWithMaxUpperBound] =sumOfRewards[advertisementWithMaxUpperBound] + rewards
        
        totalRewards = totalRewards + rewards
    
    advertisementsSelectedDataframe = pd.DataFrame(advertisementsSelected)
    
    #we need to see the last record of the below csv files. It will contains the index of the advertisement which is best among all.
    #selected advertisement index will be 4
    advertisementsSelectedDataframe.to_csv("advertisementsSelected.csv", index = False)
        
        
if __name__ == "__main__":
    trainUpperConfidenceBound()