/******************************************************************************

Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/problems/view/1076
    Online compiler -> https://onlinegdb.com/QD8tPGZ4F
    Day 8

*******************************************************************************/
#include <stdio.h>
#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

void reinicarMatriz(int matriz[50][50]){
    for(int i=0;i<50;i++){
        for(int j=0;j<50;j++){
            matriz[i][j] = 0;
        }
    }
}


int main()
{
    int testCases;
    int vert,edg,start,caminho;
    int matriz[50][50];
    
    scanf("%d",&testCases);
    while(testCases>0){
        reinicarMatriz(matriz);
        caminho =0;
        
        scanf("%d",&start);
        
        scanf("%d %d",&vert,&edg);
        
        
        for(int i=0;i<edg;i++){
            int nodeA,nodeB;
            scanf("%d %d",&nodeA,&nodeB);
            if(matriz[nodeA][nodeB]==0 || matriz[nodeB][nodeA]==0  ){
                matriz[nodeA][nodeB]++;
                matriz[nodeA][nodeB]++;
                matriz[nodeB][nodeA]++;
                matriz[nodeB][nodeA]++;
                
                caminho = caminho + 2;
                
            }
            
        }
        
        printf("%d\n",caminho);
        
        testCases--;
    }

    return 0;
}
