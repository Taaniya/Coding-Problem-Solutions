"""
Problem statement:
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. 
At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. 
The player adds the chosen number to their score. The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, 
and you should also return true. You may assume that both players are playing optimally.

E.g.,
Input: nums = [1,5,2]
Output: false

Input: nums = [1,5,233,7]
Output: true
------------------------------------------------------------------------------------------------------------------------------
Approach -
Using Dynamic programming with memoization.

This is similar to solving the problem of optimal strategy for a game.
Both players take turns. 1st Player takes turn when argument is passed as 0.
Recursive function computes score of 1st player by adding up its score at its every turn.
1st Player score is computed based on maximum of final outcome of 2 scenario - where it either picks 1st array element or the 2nd one.

The score computed by minimum of 2 final outcomes during other player's turn is eventually added to score of 1st player turn due to
recursive call in score calculation of player. Computing this score for 1st player as a minmum of 2 scenarios is equivalent to the 
opponent playing so as to maximize its own score (while minimizing 1st player's score), hence the minimum.

To keep track of score player 2 along with player 1, to identify the winner its score, every element selected by 2nd player during 
its turn is subtracted from score returned during 2nd player's turn.
This is computed 1st player's score related to 2nd player.
If this score >= 0, 1st player either has equal score as 2nd player or more than that.

The approach uses memoization to cache intermediate results.
"""

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def solve(arr: List, start: int, end: int, player: int) -> int:
            if (start >= len(arr)) or (end < 0) or (start > end):
                return 0
            if (start, end) in memo:
                return memo[(start, end)]
            if player == 0:
                score = max( arr[start] + solve(arr, start+1, end, 1),
                             arr[end] + solve(arr, start, end-1, 1)
                            )
                memo[(start, end)] = score
            else:
                # compute minimal score for main player while opponent player plays their turn
                # Also subtract opponent's score from A's score for opponent's turn to keep track of 
                # overall score difference.
                score = min(solve(arr, start+1, end, 0) - arr[start], \
                            solve(arr, start, end-1, 0) - arr[end] )
                memo[(start, end)] = score
            return memo[(start, end)]
        
        if solve(nums, 0, len(nums)-1, 0) >= 0:
            return True
        else:
            return False
