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
