/*
@author: Taaniya Arora

This code is solutions for one of the problems from Google Code Jam Contest - Round B APAC Test 2016
https://code.google.com/codejam/contest/5254487/dashboard

**Problem B -** Sherlock and Watson Gym Secrets

Watson and Sherlock are gym buddies.
Their gym trainer has given them three numbers, A, B, and N, and has asked Watson and Sherlock to pick 
two different positive integers i and j, where i and j are both less than or equal to N. Watson is 
expected to eat exactly iA sprouts every day, and Sherlock is expected to eat exactly jB sprouts every day.

Watson and Sherlock have noticed that if the total number of sprouts eaten by them on a given day is 
divisible by a certain integer K, then they get along well that day.

So, Watson and Sherlock need your help to determine how many such pairs of (i, j) exist, where i != j. 
As the number of pairs can be really high, please output it modulo 109+7 (1000000007).

Input-
The first line of the input gives the number of test cases, T. T test cases follow. Each test case 
consists of one line with 4 integers A, B, N and K, as described above.

Output-
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) 
and y is the required answer.

Limits-
1 ≤ T ≤ 100.
0 ≤ A ≤ 106.
0 ≤ B ≤ 106.

Small dataset
1 ≤ K ≤ 10000.
1 ≤ N ≤ 1000.

Large dataset
1 ≤ K ≤ 100000.
1 ≤ N ≤ 1018.

Sample
Input 
3
1 1 5 3
1 2 4 5
1 1 2 2

Output
Case #1: 8
Case #2: 3
Case #3: 0

*/

import java.util.*;
import java.io.*;
 class SproutProblem    {   
    public static void main(String args[])throws IOException,NumberFormatException
    {  int m=0,count=0,T,x,y=0,min,c=0,N,K;
     double A,B,i,j;
          int L,R;
     String fpath = "F://Downloads/B-small-attempt1.in";
        FileReader fr =new FileReader(fpath);
        FileReader fr1=new FileReader(fpath);
        int [] b =new int[800];
        String str="";
        while(fr.read()!=-1) count++;
        char [] arr =new char[count];
        fr1.read(arr);
        fr.close();
        m=0;
        i=0;
         for(char h:arr )             {
      if(Character.isDigit(h))   str=str+h;       
      else       {    
       b[m++]=Integer.parseInt(str);
       str="";            }       }       
     T=b[0];
         c=0;
    for( x=1;x<=T;x++)   //T test cases
    {  A=b[++c];
       B=b[++c];
       N=b[++c];
       K=b[++c];   
       count=0;
           for(i=1;i<=N ;i++)          {  
                for(j=1;j<=N;j++)       {
                   if(j==i) continue;
                  double temp=Math.pow(i,A)+ Math.pow(j, B) ;
                   if(temp%K==0) count++;         }              
           }   
      System.out.println("case #"+x+" count= "+count);       }     
    }
}
