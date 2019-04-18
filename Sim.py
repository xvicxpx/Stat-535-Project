import Play

def sim(n = 100, weight1 = None, weight2 = None):
    """
    Takes in a number of games n, and the weights for two dice. 
    Returns the total number of wins from n craps games
    """
    
    count = 0
    for i in range(n):
        if(Play.play_game(weight1, weight2)):
            count += 1
    return count