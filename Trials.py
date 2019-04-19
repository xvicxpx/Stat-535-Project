
import Sim as S

def trials(N = 1000, n = 100, weight1 = None, weight2 = None):
    """ 
    Takes in number of repetitions of sim, N, number of games to play in
    sim, n, and weights for the dice.
    Returns a float and a list. The float holds the win rate for the weights.
    The list holds the number of times x wins were found in N trials.
    """
    trial = [0 for i in range(n+1)]
    test_wins = 0
    total_wins = 0
    
    for test in range(N):
        test_wins = S.sim(n = n, weight1 = weight1, weight2 = weight2)
        trial[test_wins] += 1
        total_wins += test_wins
        
    win_rate = total_wins/(N*n)
    
    return [win_rate, trial]

