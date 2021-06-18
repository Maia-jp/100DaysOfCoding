/******************************************************************************

Solution by: Joao P. Maia
Problem: https://www.urionlinejudge.com.br/judge/en/problems/view/1029
online compiler: https://www.mycompiler.io/view/CAE5wCi
Day 10

*******************************************************************************/
#include <stdio.h>


int fib(int n, int* calls){
    *calls = *calls+1;
    if(n==0)
        return 0;
    if(n==1)
        return 1;
        
    int fib1 = fib(n-1,calls);
    int fib2 = fib(n-2,calls);
    
    return fib1+fib2;
    
}


int main()
{
    int testCases;
    int calls = 0;
    
    scanf("%d",&testCases);
    
    while(testCases){
        int calls = 0;
        int n,f;
        
        scanf("%d",&n);
        f = fib(n,&calls);
        printf("fib(%d) = %d calls = %d\n",n,calls-1,f);
        
        testCases--;
    }
   

    return 0;
}
