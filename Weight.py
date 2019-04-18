def getWeightList(num = None):
    """Enter a the side number lets say 5 and it will weight the dice towards a 5 and lower the weight of the oposite side
    of the dice which is going to be a 2 while keeping the other sides the same weight.
    Using the formula 2/x + 2/x + 2/x + 2/x + 1/x + 3/x = 1. 
    We can also change how heavy we want to weight the dice depending on the numerators we want to give"""

    weight_list = [None] * 5

    def pair(self):
        pair_dic = {1:6,6:1,2:5,5:2,3:4,4:3}
        return pair_dic.get(num)

    if num == None:
        weight_list = [1/6,1/6,1/6,1/6,1/6]
    else:
        for i in range(5):
            weight_list[i] = 2/12
        weight_list[num-1] = 3/12
        weight_list[pair(5) - 1] = 1/12
        
    return weight_list
    

    