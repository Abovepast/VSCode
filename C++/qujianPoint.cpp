#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long LL;
const int N=1e6+10;

struct Range {
    int l,r;

    bool operator<(const Range& W) const {
        return r<W.r;
    }

}range[N];


int main() {
    
    int n;
    cin>>n;

    for(int i=0;i<n;i++) {
        cin>>range[i].l>>range[i].r;
    }
    
    return 0;
}