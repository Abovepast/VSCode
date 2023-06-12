#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int N = 110;

int n, ans[N], b[N], flag;

struct node
{
    int t, d, l;
}a[N];

bool check(int x)
{
    int res = 0;
    for (int i = 1; i <= x; i ++)
    {
        if (res > a[ans[i]].t + a[ans[i]].d)
            return false;
        res = max(res, a[ans[i]].t);
        res += a[ans[i]].l;
    }
    return true;
}

void dfs(int sum)
{
    if (!check(sum) || flag)
        return;
    if (sum == n)
    {
        puts("YES");
        flag = 1;
    }
    for (int i = 1; i <= n; i ++)
    {
        if (!b[i])
        {
            b[i] = 1;
            ans[sum + 1] = i;
            dfs(sum + 1);
            b[i] = 0;
        }
    }
}

void solve()
{
    flag = 0;
    cin >> n;
    for (int i = 1; i <= n; i ++)
        cin >> a[i].t >> a[i].d >> a[i].l;
    dfs(0);
    if (!flag) puts("NO");
}

int main()
{
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}