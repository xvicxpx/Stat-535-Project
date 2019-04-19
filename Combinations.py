import Trials as T

def combinations(N = 1000, n = 100):
    """ 
    Takes in number of repetitions of sim, N, number of games to play in
    sim, n, for the trials function.
    Returns two dictionary created by trials, where the keys are the weights
    used in trials. The first dictionary holds the win rate, the second holds
    lists of the number of wins that were found. 
    """
    win_rate_data = {}
    win_data = {}
    trial_data = []
    
    trial_data = T.trials(N = N, n = n)
    win_rate_data[(0,0)] = trial_data[0]
    win_data[(0,0)] = trial_data[1]
    
    for die1 in range (1,7):
        
        for die2 in range (die1, 7):
            trial_data = T.trials(N = N, n = n, weight1 = die1, weight2 = die2)
            win_rate_data[(die1, die2)] = trial_data[0]
            win_data[(die1, die2)]  = trial_data[1]
        
        trial_data = T.trials(N = N, n = n, weight1 = die1)
        win_rate_data[(die1,0)] = trial_data[0]
        win_data[(die1, 0)] = trial_data[1]
        
    return [win_rate_data, win_data]