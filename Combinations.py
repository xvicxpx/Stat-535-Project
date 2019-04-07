def combinations(N = 1000, n = 100):
    """ 
    Takes in number of repetitions of sim, N, number of games to play in
    sim, n, for the trials function.
    Returns a dictionary of lists created by trials, where each key is the 
    weighting used in trials.
    """
    data = {}
    win_list = []
    
    win_list = trials(N = N, n = n)
    data[(0,0)] = win_list
    
    for die1 in range (1,7):
        
        for die2 in range (die1, 7):
            win_list = trials(N = N, n = n, weight1 = die1, weight2 = die2)
            data[(die1, die2)]  = win_list
        
        win_list = trials(N = N, n = n, weight1 = die1)
        data[(die1, 0)] = win_list
        
    return data