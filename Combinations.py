def combinations(N = 1000, n = 100):
    """ 
    N = how many times will run
    n = how many time run Sim()
    will collect all the data into a dictionary of lists
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