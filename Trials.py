import Sim as S

def trials(N = 1000, n = 100):
    """ 
    N = how many times will run
    n = how many time run Sim()
    will collect all the data into a dictionary of lists
    """
    data = {}
    trial = [0 for i in range(n+1)]
    test_wins = 0
    
    for test in range(N):
        test_wins = S.sim(n = n)
        trial[test_wins] += 1
    
    data[(0,0)] = trial
    
    for die1 in range (1,7):
        
        for die2 in range (die1, 7):
            trial = [0 for i in range(n+1)]
            
            for test in range(N):
                test_wins = S.sim(n = n, weight1 = die1, weight2 = die2)
                trial[test_wins] += 1
                
            data[(die1, die2)] = trial
        
        trial = [0 for i in range(n+1)]    
        
        for test in range(N):
            test_wins = S.sim(n = n, weight1 = die1)
            trial[test_wins] += 1 
            
        data[(die1, 0)] = trial
        
    return data