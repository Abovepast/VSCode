#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long LL;
const int N=1e6+10;

int main() {
    
    int n;
    cin>>n;

    long long sum = 1;
    for(int i=1;i<=n;i++) {
        sum*=i;
    }

    cout<<n<<"的阶乘是："<<sum<<endl;

    return 0;
}