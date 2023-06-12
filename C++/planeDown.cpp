#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long LL;
const int N=10;

int n;

struct Plane
{
    int t, d, l;
    /* data */
}p[N];

bool st[N];

bool dfs(int u,int last) {
    if(u==n) return true;

    for(int i=0;i<n;i++) {
        int t=p[i].t, d=p[i].d, l=p[i].l;
        if(!st[i] && t+d >=last) {
            st[i] = true;

            if(dfs(u+1, max(last,t)+1))
                return true;
            st[i] = false;
        }
    }

    return false;
}

int main() {
    int T;
    scanf("%d",&T);

    for(int i=0;i<n;i++) {
        int t,d,l;
        scanf("%d%%d%d", &t, &d, &l);
        p[i] = {t, d, l};
    }

    memset(st, 0, sizeof st);
    if(dfs(0,0)) puts("YES");
    else puts("NO");
    
    
    return 0;
}