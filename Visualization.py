#Visualization 

"""
Takes a dictionary of lists
Creates a new Dictionary with the same keys but values are the average of the lists of the original
Then plots them in a bar plot

After examination we will make graphs of the best and worst performances
"""
import matplotlib.pyplot as plt
import Combinations as c

rates_dict = {}
testDict = c.combinations(N=100, n=10)[0]

plt.bar(range(len(testDict)), list(testDict.values()), align='center')
plt.xticks(range(len(testDict)), list(testDict.keys()), rotation = 'vertical')
plt.ylim([0.4 , 0.6])