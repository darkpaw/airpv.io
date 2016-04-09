# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 11:03:31 2016

@author: hargh
"""

import pandas as pd
import numpy as np

class Household:
    def __init__(self, LoadProfile, WTPProfile, GridProfile, MarketProfile):
        self.LoadProfile = LoadProfile
        self.WTPProfile = WTPProfile
        self.GridProfile = GridProfile
        self.MarketProfile = MarketProfile
        
        self.Bill = 0

class Generator:
    def __init__(self, GenProfile, WTSProfile, GridProfile, MarketProfile):
        self.GenProfile = GenProfile
        self.WTSProfile = WTSProfile
        self.GridProfile = GridProfile
        self.MarketProfile = MarketProfile
          
        self.Bill = 0

class Market:
    def __init__(self, Intervals):
        self.Quantity = np.zeros(Intervals)
        self.Price = np.zeros(Intervals)
        
def HouseholdConstructor(LoadProfiles, WTPProfiles):
    #Constructs households

    i=0
    for i in range(0,len(LoadProfiles.columns)):
        LoadProfile = LoadProfiles.iloc[:, i].values
        WTPProfile = WTPProfiles.iloc[:, i].values
        GridProfile = LoadProfile
        MarketProfile = np.zeros(len(GridProfile))
        
        Households[i] = Household(LoadProfile, WTPProfile, GridProfile, MarketProfile)
    
        #a = Household(LoadProfiles.iloc[:, 0].values, WTPProfiles.iloc[:, 0].values, LoadProfiles.iloc[:, 0].values, np.zeros(48))
        #b = Household(LoadProfiles.iloc[:, 1].values, WTPProfiles.iloc[:, 1].values, LoadProfiles.iloc[:, 1].values, np.zeros(48))
    return Households


        
def GeneratorConstructor(GenProfiles, WTSProfiles):
    #Constructs generators

    i=0
    for i in range(0,len(GenProfiles.columns)):
        GenProfile = GenProfiles.iloc[:,i].values
        WTSProfile = WTSProfiles.iloc[:,i].values
        GridProfile = GenProfile
        MarketProfile = np.zeros(len(GridProfile))
        
        Generators[i] = Generator(GenProfile, WTSProfile, GridProfile, MarketProfile)
    
    return Generators

def MarketConstructor(Intervals):
    #Constructs market
    TheMarket = Market(Intervals)

    return TheMarket
    
def Allocation():
    #Allocates PV gen to households 

    #For each 30min interval, find:
    #1. The market clearing price
    #2. The market clearing quantity
    #3. The household loads satisfied by the PV system
    #4. The household loads that must be served by the grid
    #5. The PV generation bought by the households
    #6. The PV generation exported to teh grid
    
    for j in range(0, len(TheMarket.Price)):
    
        Priority = pd.DataFrame(data=np.zeros((len(Households),2)), columns = ['WTP', 'Load'])
        
        #Rank households based on their WTP
        for i in range(0, len(Households)):
            
            Priority.iloc[i,0] = Households[i].WTPProfile[j]
            Priority.iloc[i,1] = Households[i].LoadProfile[j]
        
        Priority.sort(columns = 'WTP', ascending = False, inplace = True)
        
        #Allocate PV gen to households based on rank
        for i in range(0, len(Households)):
            
            #Case where no PV generation           
            if Generators[0].GenProfile[j] == 0:
                TheMarket.Quantity[j] = 0
                TheMarket.Price[j] = 0
                Households[Priority.index.values[i]].MarketProfile[j] = 0
                Households[Priority.index.values[i]].GridProfile[j] = Priority.iloc[i,1]
                Generators[0].GridProfile[j] = 0
                
            #Case where PV can meet all of Household i's demand and Generators's WTS <= Household's WTP
            elif TheMarket.Quantity[j] + Priority.iloc[i,1] <= Generators[0].GenProfile[j] and Generators[0].WTSProfile[j] <= Priority.iloc[0,0]:
                
                TheMarket.Quantity[j] += Priority.iloc[i,1]
                TheMarket.Price[j] = Priority.iloc[i,0]
                Households[Priority.index.values[i]].MarketProfile[j] = Priority.iloc[i,1]
                Households[Priority.index.values[i]].GridProfile[j] = 0
                Generators[0].GridProfile[j] -= Priority.iloc[i,1]
                 
            #Case where PV can partially/not meet Household i's demand and Generators's WTS <= Household's WTP
            elif TheMarket.Quantity[j] + Priority.iloc[i,1] > Generators[0].GenProfile[j] and Generators[0].WTSProfile[j] <= Priority.iloc[0,0]:
            
                Households[Priority.index.values[i]].MarketProfile[j] = Generators[0].GenProfile[j] - TheMarket.Quantity[j]
                Households[Priority.index.values[i]].GridProfile[j] = Priority.iloc[i,1] - (Generators[0].GenProfile[j] - TheMarket.Quantity[j])
                TheMarket.Quantity[j] = Generators[0].GenProfile[j]
                TheMarket.Price[j] = Priority.iloc[i,0]
                Generators[0].GridProfile[j] = 0
                break    
     
#Main

#Import household load profiles
LoadProfiles = pd.read_csv("/Users/hargh/Desktop/CSIRO/Loads.csv", sep = ',')
    
#Import Willingness to Pay profiles
WTPProfiles = pd.read_csv("/Users/hargh/Desktop/CSIRO/WTP.csv", sep = ',')

Households = {}    
Households = HouseholdConstructor(LoadProfiles, WTPProfiles)

#Import PV gen profiles
GenProfiles = pd.read_csv("/Users/hargh/Desktop/CSIRO/PV.csv", sep = ',')

#Import Willing to Sell profiles
WTSProfiles = pd.read_csv("/Users/hargh/Desktop/CSIRO/WTS.csv", sep = ',')

Generators = {}
Generators = GeneratorConstructor(GenProfiles, WTSProfiles)

#Set number of intervals
Intervals = 48
TheMarket = MarketConstructor(Intervals)

Allocation()


 


    
    
    
    
    
    
    
