#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Taaniya

"""
This code implements a greedy algorithm to solve the Ben the gamer problem from TechGig CodeGladiators 2018.
Ben is one of the best gamers in India. He also happens to be an excellent programmer. 
So, he likes to play games which require use of both gaming skills as well as programming
 skills. One such game is SpaceWar.

In this game there are N levels and M types of available weapons. The levels are numbered 
from 0 to N-1 and the weapons are numbered from 0 to M-1. Ben can clear these levels in any 
order. In each level, some subset of these M weapons is required to clear this level. If in 
a particular level, Ben needs to buy x new weapons, he will pay x² coins for it. Also note 
that Ben can carry all the weapons he has currently to the next level. Initially, 
Ben has no weapons. Can you tell the minimum coins required such that Ben can clear all 
the levels.

Input Format
The first line of input contains 2 space separated integers;
N - the number of levels in the game and M - the number of types of weapons.
N lines follows. The ith of these lines contains a binary string of length M. If the jth character of this string is 1 , it means we need a weapon of type j to clear the ith level.
Constraints
1 <= N <=20
1<= M <= 20
Output Format
Print a single integer which is the answer to the problem.

Sample Test Case 1
Input
1 4
010
1
Output
4
Explanation
There is only one level in this game. We need 2 types of weapons - 1 and 3. Since, 
initially Ben has no weapons he will have to buy these, which will cost him 2² = 4 coins.

Sample Test Case 2
Input
3 3
111
001
010

Output
3

"""
def main():
    inp = input()
    inp_list = inp.split()
    N = int(inp_list[0])
    M = int(inp_list[1])
    weapon_list = []
    
    for i in range(N):
        level = input()
        weapon_list.append([level,int(level.count("1"))])
        
    # sort levels w.r.t no. of weapons required in each of them    
    sorted_wlist = sorted(weapon_list,key=lambda ele: ele[1])

    have = []
    want_count = 0
    requirement_list = []   
    
    # To begin with, we will always choose the level requiring the least no. of 
    # weapons since we donot have any weapons already.
    # Adding the first weapons info from the above sorted list into the final sorted list

    for ind,weapons_info in enumerate(sorted_wlist):
        strng = weapons_info[0]
        want_count = 0
        # Get indices of weapons required in each level
        for weapon_type,char in enumerate(strng):
            if char=="1":
                # Check if Ben already has the required weapon               
               if weapon_type not in have:
                   want_count+=1
                   have.append(weapon_type)
        
        # Maintaining list of weapons required and those that Ben already has 
        # For every level, the list of weapons that Ben already has, 
        # grows as more get accumulated
        requirement_list.append([strng, want_count,len(have)])
        
        
   
    final_level_order = []
    
    # To begin with, we will always choose the level requiring the least no. of 
    # weapons since we donot have any weapons already.
    # Adding the first weapons info from the above sorted list into the final sorted list
    # weapons info - weaponse binary string,no. of weaponse wanted out all them, 
    # excluding those that Ben already has which is 0 in the beginning
    
    final_level_order.append([requirement_list[0][0],requirement_list[0][1],requirement_list[0][2]])
    
    requirement_list.pop(0)         # remove the first level
    
    # Using greedy approach, choose subsequent levels from the list in which no. 
    # of weapons wanted (i.e want_count) is the lowest.
    
    while len(requirement_list) != 0 :
        want_count = []
        for weapons_info in requirement_list:
            want_count.append(weapons_info[1])
        
        level = want_count.index(min(want_count))
        final_level_order.append([requirement_list[level][0],requirement_list[level][1],requirement_list[level][2]])
        requirement_list.pop(level)
        
    num_coins = sum(i[1]**2 for i in final_level_order)
    print(num_coins)
    return num_coins
    

main()
                    
