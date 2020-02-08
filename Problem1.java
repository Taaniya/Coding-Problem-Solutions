/*
@author: Taaniya Arora

This code is solutions for one of the problems from Google Code Jam Contest - Round B APAC Test 2016
https://code.google.com/codejam/contest/5254487/dashboard

**Problem A** - Sherlock and Parentheses

Sherlock and Watson have recently enrolled in a computer programming course. Today, the tutor taught them 
about the balanced parentheses problem. A string S consisting only of characters ( and/or ) is balanced if:
It is the empty string, or:
It has the form (S), where S is a balanced string, or:
It has the form S1S2, where S1 is a balanced string and S2 is a balanced string.

Sherlock coded up the solution very quickly and started bragging about how good he is, so Watson gave him 
a problem to test his knowledge. He asked Sherlock to generate a string S of L + R characters, in which 
there are a total of L left parentheses ( and a total of R right parentheses ). Moreover, the string must 
have as many different balanced non-empty substrings as possible. (Two substrings are considered different 
as long as they start or end at different indexes of the string, even if their content happens to be the same).
Note that S itself does not have to be balanced.

Sherlock is sure that once he knows the maximum possible number of balanced non-empty substrings, he will be 
able to solve the problem. Can you help him find that maximum number?

Input-
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists 
of one line with two integers: L and R.

Output-
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) 
and y is the answer, as described above.

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

Sample
Input 
3
1 0
1 1
3 2

Output
Case #1: 0
Case #2: 1
Case #3: 3

*/

import java.util.*;
import java.io.*;
 class Balanced  {   
    public static void main(String args[])throws IOException,NumberFormatException
    {  int i=0,m=0,count=0,T,x,y=0,min,cs=0;
          int L,R;
         String fpath = "F://Downloads/A-large.in";
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
         for(char h:arr )            {
      if(Character.isDigit(h))   str=str+h;       
      else         {    
       b[i++]=Integer.parseInt(str);
       str="";         }
   }          
T=b[0];
  i=0;
    for( x=1;x<=T;x++)   //T cases        
    {       
       L=b[++i];
       R=b[++i];
       if(L<R) min=L; else min=R;            
           y=0;
        for(int l=1; l<=min;l++)         {        
         y=y+l;         }  
       System.out.println("Case #"+x+": "+y);      
     }
/*in every case there will be D number of '()' substrings where D is min(L,R) .
   To find max number of substring using combination of subsequences   */     
   }
}
