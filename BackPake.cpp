#include<iostream>
#include<cmath>
using namespace std;

// 0-1背包问题c++实现

int backPake(int w[],int v[],int m,int num){
    int dp[num+1][m+1];
    for(int i=0;i<=m;i++){
        dp[0][i]=0;
    }
    for(int i=0;i<num;i++){
        for(int j=0;j<=m;j++){
            if(w[i]>j){
                dp[i+1][j]=dp[i][j];
            }else{
                dp[i+1][j]=max(dp[i][j],dp[i][j-w[i]]+v[i]);
            }
        }
    }
    return dp[num][m];
};

int main(){
    int w[]={2,3,4,5};
    int v[]={3,4,5,6};
    int m = 8;
    int num = 4;
    cout<<backPake(w,v,m,num)<<endl;
    return 0;
}