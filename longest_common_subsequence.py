#! /bin/usr/env python

"""
This script implements function to find longest common subsequence for given 2 sequences.

Problem statement: 
Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, 
but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
And "ace" is a subsequence of "abcde", with length 3.
    
    Reference: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
    
Time complexity - Best case is when the 2 sequences are identical - O(1)
Worst case - When no character matches in the sequences.
Brute force resursive approach takes time of order - O(2^n). (Recursion tree for given example illustrated in this repo. Refer README)
Using DP & memoization, O(n * m)

Space complexity - O(m*n)
"""

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
    
