#! /bin/usr/env python

def lcs_len(X,Y,memo=None) : 
    """
    Finds the length of longest common subsequence.
    
    Parameters:
    ----------------------
    X - List(str)
    Y - List(str)
    memo = empty dictionary of tuple and integer pairs holding length of longest 
           subsequence for a pair strings in a tuple
    
    Returns:
    ----------------------
    int - length of longest common subsequence
    
    eg.
    >> lcs_len('BCDA','BAC')
    >> 2
    
    >> lcs_len("ABCBDAB","BDCABA")
    >> 4
    """
    m = len(X)
    n = len(Y)

    if memo is None:
        memo = dict()
        
    if (X,Y) in memo:
        return memo[(X,Y)]

    elif ((m == 0) or (n == 0)):
        memo[(X,Y)] = 0

    elif X[0] == Y[0] :
        memo[(X,Y)] = 1 + lcs_len(X[1:], Y[1:], memo)

    else : 
        memo[(X,Y)] = max(lcs_len(X[1:], Y, memo), lcs_len(X, Y[1:], memo)) 

    return memo[(X,Y)]
    
