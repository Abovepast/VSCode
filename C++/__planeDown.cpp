/*飞机降落AC代码*//*(但AcWing没过)*/

#include <iostream>
 
using namespace std;
const int N = 12;
int T, t[N], d[N], l[N], n, a[N];
bool vis[N], k;
 
bool check(void) {
    int tt = t[a[1]];
    for (int i = 1; i <= n; i++) {
        int index = a[i];
        if (t[index] + d[index] < tt) return false;
        else tt = max(tt, t[index]) + l[index];
    }
    return true;
}
 
void dfs(int cnt) {
    if (k) return;
    if (cnt == n+1) {
        if(check()) k = true;
        return;
    }
    for (int i = 1; i <= n; i++)
        if (!vis[i]) {
            a[cnt] = i;

            vis[i] = true;
            dfs(cnt + 1);
            vis[i] = false;
        }
}
 
int main() {
    cin >> T;
    while (T--) {
        cin >> n;
        for (int i = 1; i <= n; i++) cin >> t[i] >> d[i] >> l[i];
        k = false;
        dfs(1);
        if (k)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}