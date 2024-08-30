#! /user/bin/env python
"""
Problem statement:
Consider a row of N coins of values V1 . . . Vn, where N is even. We play a game against an opponent by alternating turns. 
In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin.
Determine the maximum possible amount of money we can definitely win if we move first.

Note: The opponent is as clever as the user.
"""

def computeTotal(arr):
    """
    This function computes maximum possible amount of money we can definitely win if we move first 
    in a game of n even coins where the players take alternate turns to select either the 
    first or last coin, remove it permanently and earn the value of the coin.
    
    Reference:
    https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
    
    The solution is implemented using Dynamic Programming approach and memoization.
    eg. 
    >> computeTotal([2,8,15,7])
    >> 17
    >>
    >> computeTotal([2,5,8,20])
    >> 25
    >>
    >> computeTotal([1, 2, 5, 8, 20, 15, 4, 35])
    >> 61
    """
    # create a dictionary maintaining the maximum amount collected with coins between
    # start and end indices. We just need to store the best result ( highest amount of money 
    # that can be collected from the coins between start and end indices )    
    lookup = dict()
    
    def getSum(arr, start, end):
        """
        IP = [2, 8, 15, 7]
        OP = 2 + 15 = 17

        IP = [1,2,3,4]
        OP = 4, 2 = 6
        """
        # play our chance
        if (end - start ) == 1:
            # If only 2 coins are present in the game, choose greedily.
            lookup[(start, end)] = arr[start] if arr[start] > arr[end] else arr[end]

        elif (start,end) in lookup :            
            return lookup[(start, end)]

        else:
            # Play our chance, both ways, & cleverly play opponent both ways
            # Get minimum of the 2 possibilities of opponent's turn, if we choose left coin
            left = arr[start] + min(getSum(arr, start+1, end-1), getSum(arr, start+2, end))
            
            # Get minimum of the 2 possibilities of opponent's turn, if we choose right coin
            right = arr[end] + min( getSum(arr, start+1, end-1), getSum(arr, start, end-2))
            
            # get the max value of the 2 possibilities of choosing right & left coin
            lookup[(start, end)] = max(left, right)
        
        return lookup[(start, end)]
    score = getSum(arr,0,len(arr)-1)
    return score
