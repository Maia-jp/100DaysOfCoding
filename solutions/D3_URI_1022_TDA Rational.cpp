/******************************************************************************

Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/problems/view/1022
    Online compiler -> https://onlinegdb.com/rkMcszo_d
    Day 3

*******************************************************************************/
#include <stdio.h>
#include <iostream>

using namespace std;

//Euclidian
int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int main()
{
    int testCases;
    cin >> testCases;
    while(testCases){
        int D1,N1,D2,N2,OD1,ON1;
        char sign;
        
        scanf("%d / %d %c %d / %d",&N1,&D1,&sign,&N2,&D2);
        
       if(sign == '+'){
           OD1 = N1*D2 + N2*D1;
           ON1 = D1 * D2;
       }
       if(sign == '-'){
           OD1 = N1*D2 - N2*D1;
           ON1 = D1*D2;
       }
       if(sign == '*'){
           OD1 = N1*N2;
           ON1 = D1*D2;
       }
       if(sign == '/'){
           OD1 = N1*D2;
           ON1 = N2*D1;
       }
       
       int GCD = abs(gcd(OD1,ON1));
       if(GCD==1){
           printf("%d/%d = %d/%d",OD1,ON1,OD1,ON1);
       }else{
           printf("%d/%d = %d/%d",OD1,ON1,OD1/GCD,ON1/GCD);
       }
       cout<<endl;
       
    testCases--;
    }

    return 0;
}
