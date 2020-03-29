#! /user/bin/env python

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
    maximum = 0
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
        nonlocal maximum           
        
        if (end - start + 1) % 2 == 1:
             # play the opponent when # coins are odd
            if arr[start] > arr[end]:
                start += 1
            else:
                end -= 1
        
        # play our chance
        if (end - start ) == 1:
            # If only 2 coins are present in the game, choose greedily.
            lookup[(start, end)] = arr[start] if arr[start] > arr[end] else arr[end]

        elif (start,end) in lookup :            
            return lookup[(start, end)]

        else:
            # Play our chance , both ways.
            # Get max money that can be collected from the remaining if we choose the left most now
            left = arr[start] + getSum(arr, start+1, end)
            
            # Get max money that can be collected from the remaining if we choose the right most now  
            right = arr[end] + getSum(arr, start, end -1)
            lookup[(start, end)] = max(left, right)
            maximum = max(maximum, lookup[(start, end)])

        return lookup[(start, end)]
    _ = getSum(arr,0,len(arr)-1)
    return maximum
