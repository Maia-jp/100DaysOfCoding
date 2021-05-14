/******************************************************************************
    Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/problems/view/1152
    Online compiler -> https://onlinegdb.com/-7d_wdAEQ
    Day 4
*******************************************************************************/
#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <tuple>
using namespace std;



int find(int vec[], int a){
    if(vec[a] == a)
        return a;
    return find(vec,vec[a]);
}


int same (int vec[], int a,int b){
    return find(vec,a) == find(vec,b);
}

// a class -> b class
void uni(int vec[],int a,int b){
   int p,q;
   p = find(vec,a);
   q = find(vec,b);
   vec[p] = vec[q];

}

bool sortbyth(const tuple<int, int, int>& a, 
              const tuple<int, int, int>& b){
    return (get<2>(a) < get<2>(b));
}


int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n) && (m+n)){
       int v1,v2,w,totalSize,saveSize;
       totalSize =0;
       saveSize =0;
       int v[m];
       for(int i=0;i<m;i++){
           v[i] = i;
       }
       
       
       vector<tuple<int,int,int>> ipt;
       for(int i=0;i<n;i++){
           scanf("%d %d %d",&v1,&v2,&w);
           totalSize = totalSize + w;
           ipt.push_back(make_tuple(v1,v2,w));
       }
       sort(ipt.begin(), ipt.end(), sortbyth);
       
       for(auto t:ipt){
           if(!same(v,get<0>(t),get<1>(t))){
               saveSize = saveSize + get<2>(t);
               uni(v,get<0>(t),get<1>(t));
           }
       }
       
       cout<<totalSize-saveSize<<endl;
       
       
    }

    return 0;
}
