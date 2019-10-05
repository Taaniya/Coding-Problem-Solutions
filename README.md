# Google-Code-Jam-Problems
This repository contains solutions to two of the problems from Google Code Jam 

**Problem A**

Sherlock and Watson have recently enrolled in a computer programming course. Today, the tutor taught them about the balanced parentheses problem. A string S consisting only of characters ( and/or ) is balanced if:
It is the empty string, or:
It has the form (S), where S is a balanced string, or:
It has the form S1S2, where S1 is a balanced string and S2 is a balanced string.

Sherlock coded up the solution very quickly and started bragging about how good he is, so Watson gave him a problem to test his knowledge. He asked Sherlock to generate a string S of L + R characters, in which there are a total of L left parentheses ( and a total of R right parentheses ). Moreover, the string must have as many different balanced non-empty substrings as possible. (Two substrings are considered different as long as they start or end at different indexes of the string, even if their content happens to be the same). Note that S itself does not have to be balanced.

Sherlock is sure that once he knows the maximum possible number of balanced non-empty substrings, he will be able to solve the problem. Can you help him find that maximum number?
Input-
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of one line with two integers: L and R.
Output-
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the answer, as described above.
Limits-
1 ≤ T ≤ 100.
Small dataset-
0 ≤ L ≤ 20.
0 ≤ R ≤ 20.
1 ≤ L + R ≤ 20.
Large dataset-
0 ≤ L ≤ 105.
0 ≤ R ≤ 105.
1 ≤ L + R ≤ 105.
 
 
 
**Problem B -**

Watson and Sherlock are gym buddies.
Their gym trainer has given them three numbers, A, B, and N, and has asked Watson and Sherlock to pick two different positive integers i and j, where i and j are both less than or equal to N. Watson is expected to eat exactly iA sprouts every day, and Sherlock is expected to eat exactly jB sprouts every day.

Watson and Sherlock have noticed that if the total number of sprouts eaten by them on a given day is divisible by a certain integer K, then they get along well that day.

So, Watson and Sherlock need your help to determine how many such pairs of (i, j) exist, where i != j. As the number of pairs can be really high, please output it modulo 109+7 (1000000007).
Input-
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of one line with 4 integers A, B, N and K, as described above.
Output-
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the required answer.
Limits-
1 ≤ T ≤ 100.
0 ≤ A ≤ 106.
0 ≤ B ≤ 106.
Small dataset
1 ≤ K ≤ 10000.
1 ≤ N ≤ 1000.
