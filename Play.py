import Dice

def play_game(weight1 = None, weight2 = None):
    """ returns true when you win and false when you lose"""
    sum = Dice.roll(weight1, weight2)
    if(sum == 2 | sum == 3 | sum == 12):
        return True
    elif(sum == 7 | sum == 11):
        return False
    else:
        while(True):
            hold = Dice.roll(weight1, weight2)
            if(hold == sum):
                return True
            if(hold == 7):
                return False