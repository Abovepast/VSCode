#include <iostream>
#include <cmath>
#include <algorithm>

typedef long long  LL;
using namespace std;

LL qmi(LL a,LL b,LL mode) {
    LL sum=1;

    a%=mode;
    while(b!=0) {
        if((b&1)==1) {
            sum=(sum*a)%mode;
        }
        b=b>>1;
        a=(a*a)%mode;
    }

    return sum;
}

int main() {
    LL a=9223372036854775807,b=a,mode=233333;
    
    cout<<"余数为"<<qmi(a,b,mode)<<endl;
    cout<<"long是"<<sizeof(long)<<"字节"<<endl;
    cout<<"int是"<<sizeof(int)<<"字节"<<endl;
    return 0;
}