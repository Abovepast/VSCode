#include <iostream>

using namespace std;

const int N = 10;

int n;
int path[N];
bool state[N]={0};

void dfs(int u)
{
    if (u > n)
    {
        for (int i = 1; i <= n; i ++ ) cout<<path[i]<<" ";
        cout<<endl;

        return;
    }

    for (int i = 1; i <= n; i ++ )
        if(!state[i]) {
            path[u] = i;

            state[i]=true;
            dfs(u+1);
            state[i]=false;
        }
}

int main()
{
    scanf("%d", &n);

    dfs(1);

    return 0;
}

