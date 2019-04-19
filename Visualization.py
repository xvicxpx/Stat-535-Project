#Visualization 

"""
Takes a dictionary of lists
Creates a new Dictionary with the same keys but values are the average of the lists of the original
Then plots them in a bar plot

After examination we will make graphs of the best and worst performances
"""

import matplotlib.pyplot as plt
import statistics
import Combinations as c

rates_dict = {}
testDict = c.combinations(N=100, n = 10)[0]

def rateDic(dictionary):
    for x in dictionary:
        rates_dict[x] = statistics.mean(dictionary[x]) 
    return rates_dict


newDict = rateDic(testDict)

plt.bar(range(len(newDict)), list(newDict.values()), align='center')
plt.xticks(range(len(newDict)), list(newDict.keys()))
