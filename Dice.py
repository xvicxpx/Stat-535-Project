import random
import numpy

def Dice(weight1, weight2):
    """ weight1 and weight 2 will be a list 
        [1,2,3,4,5,6] for normal and a weighted dice will be [1,2,3,4,5,6,6,6,6,6,6]
        Then select randomly from the list for the dice results. 
        Returns the sum of the two dices """
    # norm_dice = [1,2,3,4,5,6]
    # rand = 
    if (weight1 == null && weight2 == null)
        return(random.randint(1,6), random.randint(1,6))
    elif(weight1 != null)
        return(weight1_func(weight1), random.randint(1,6))
    elif(weight2 != null)
        return(random.randint(1,6), weight1_func(weight2))
    else
        return(both_weighted(weight1,weight2))
    
    

def weight1_func():
    diceroll = 6 # ... add function here
    
    
    return(diceroll)

def both_weighted():
    diceroll1 = 6 # .......some_function...
    diceroll2 = 6 # ....some_other function
    
    
    return(diceroll_1, diceroll_2)


