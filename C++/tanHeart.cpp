/*区间选点*/
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 100010;

int n;
struct Range
{
    int l, r;
    // bool operator< (const Range &W)const
    // {
    //     return r < W.r;
    // }

}range[N];

bool cmp(Range a,Range b) {
    return a.r<b.r;
}

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ) scanf("%d%d", &range[i].l, &range[i].r);

    sort(range, range + n, cmp);

    int res = 0, ed = -2e9;
    for (int i = 0; i < n; i ++ )
        if (range[i].l > ed)
        {
            res ++ ;
            ed = range[i].r;
        }

    printf("%d\n", res);

    return 0;
}
