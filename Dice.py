import Weight as W
import random as R

def roll(weight1 = None, weight2 = None):
    weightlist1 = W.getWeightList(weight1)
    weightlist2 = W.getWeightList(weight2)

    return weightlist1[R.randint(0,5)] + weightlist2[R.randint(0,5)]