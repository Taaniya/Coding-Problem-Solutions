#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Taaniya

"""

This code implements solution the Ruby necklace problem from TechGig CodeGladiators 2018.
Greedy approach can be observed when the cases for adding green and yellow 
rubies are interchanged when the input is 1 1 1 1.
if you add y before g, you won't be able to add green after y.
but if you add g before y, you can add y with the necklace ending with a green 
ruby.

It is the wedding day of Sanchi, the beautiful princess of Byteland. Her fiance Krishna is planning to gift her an 
awesome ruby necklace. Krishna has currently b-blue rubies, g-green rubies, r-red rubies and y-yellow rubies. He has to 
arrange the rubies next to each other in a straight line to make the necklace. But, there are a couple of rules to be 
followed while making this necklace:

A blue ruby should be followed by either a blue ruby or a red ruby
A green ruby should be followed by either a green ruby or a yellow ruby
A red ruby should be followed by either a green ruby or a yellow ruby
A yellow ruby should be followed by either a blue ruby or a red ruby
If it is possible, we should always start a necklace with a blue or a red ruby
Can you tell what is the maximum possible length of the necklace that Krishna can make. The length of a necklace 
is the number of rubies in it.

Input Format
The first line contains an integer representing b
The second line contains an integer representing r
The third line contains an integer representing y
The fourth line contains an integer representing g

Constraints
0 <= b, r, y, g <= 2000
At least one of b, r, y, g is greater than 0

Output Format
A single integer which is the answer to the problem.

Sample Test case 1
Input
1
1
1
0

Output
3

Example
One such necklace is Blue Red Green.

Sample TestCase 2
Input

1
1
1
1
Output

4
Example

One such necklace is Blue Red Green Yellow.

"""

def main(inp):
    b,r,y,g = inp[0],inp[1],inp[2],inp[3]
    
    total = b + r + y + g
    #print("total {}".format(total))
    seq = ""
    while(b+r+g+y)!=0:
        oldseq = seq
        
        if(seq=="" or seq.endswith("b") or seq.endswith("y")) and (b!=0):
            seq+="b"
            b-=1
            
        elif(seq=="" or seq.endswith("b") or seq.endswith("y")) and (r!=0):
            seq+="r"
            r-=1
         
        elif(seq=="" or seq.endswith("g") or seq.endswith("r")) and (g!=0):
            seq+="g"
            g-=1
            
        elif(seq=="" or seq.endswith("g") or seq.endswith("r")) and (y!=0):    
            seq+="y"
            y-=1
          
        elif(seq==oldseq):
            break
    
    print(seq)    
    return len(seq)


print(main([2,1,1,1]))