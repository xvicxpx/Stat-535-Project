def trials(N = 1000, n = 100, weight1 = none, weight2 = none):
    """ 
    Takes in number of repetitions of sim, N, number of games to play in
    sim, n, and weights for the dice.
    Returns a list storeing the number of times x wins were found in N trials.
    """
    trial = [0 for i in range(n+1)]
    test_wins = 0
    
    for test in range(N):
        test_wins = sim(n = n, weight1 = weight1, weight2 = weight2)
        trial[test_wins] += 1
        
    return trial