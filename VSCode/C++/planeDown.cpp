#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long LL;
const int N=1e6+10;

int T[N],D[N],L[N];
bool flag[N]={0};

void Psort(int T[],int D[],int L[],int n) {

    for(int i=0;i<n;i++)
        for(int j=1;j<n;j++) {
            if((D[i]+T[i]>D[j]+T[j])) {
                swap(T[i],T[j]);
                swap(D[i],D[j]);
                swap(L[i],L[j]);
            }
        }
    for(int i=0;i<n-1;i++)
        if(T[i]>D[i]) {
            swap(T[i],T[i+1]);
            swap(D[i],D[i+1]);
            swap(L[i],L[i+1]);
        }
    

}

void dfs(int cnt) {
    
}

int main() {
    
    int t,n;
    scanf("%d%d",&t,&n);

    int t1=t;
    int fi = 0;
    while (t--) {

        int max=0,min=0;

        for (int i=0; i<n;i++) {
            scanf("%d%d%d",&T[i],&D[i],&L[i]);
            if(max<=D[i]) max=D[i];
            if(min>=T[i]) min=T[i];
        }

        Psort(T,D,L,n);

        int et = min;
        for(int i=0; i<n; i++) {
            if(et<T[i]) et=T[i]+L[i];
            else et+=L[i];
        }

        if(et<=max) flag[fi]=true;
        fi++;

    }
    
    for(int i=0; i<fi; i++)
        if(flag[i]) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;

    return 0;
}