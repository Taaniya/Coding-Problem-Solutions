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
    for( x=1;x<=T;x++)   //T cases        {       
       L=b[++i];
       R=b[++i];
       if(L<R) min=L; else min=R;            
           y=0;
        for(int l=1; l<=min;l++)         {        
         y=y+l;         }  
       System.out.println("Case #"+x+": "+y);      }
/*in every case there will be D number of '()' substrings where D is min(L,R) .
   To find max number of substring using combination of subsequences   */     
   }
}
