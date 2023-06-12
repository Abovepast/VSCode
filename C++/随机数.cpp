#include <iostream>
#include <cmath>
#include <algorithm>
#include <time.h>

using namespace std;
typedef long long LL;
const int N=1e6+10;

int main() {
    
    srand((unsigned)time(NULL));

    int n=10,b;
    while(n--) {
        b=rand()%20+1;  //生成1~20的随机数
        cout<<b<<" ";
    }
    
    return 0;
}