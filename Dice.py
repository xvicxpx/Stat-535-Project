import Weight as W
import random as R
import numpy as np

def roll(weight1 = None, weight2 = None):
    weightlist1 = W.getWeightList(weight1)
    weightlist2 = W.getWeightList(weight2)
    list1 = np.random.choice(a=[1,2,3,4,5,6], size=10000, p=weightlist1)
    list2 = np.random.choice(a=[1,2,3,4,5,6], size=10000, p=weightlist2)
    return list1[R.randint(0,len(list1) - 1)] + list2[R.randint(0,len(list2) - 1)]