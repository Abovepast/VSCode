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
    
    cout<<"����Ϊ"<<qmi(a,b,mode)<<endl;
    cout<<"long��"<<sizeof(long)<<"�ֽ�"<<endl;
    cout<<"int��"<<sizeof(int)<<"�ֽ�"<<endl;
    return 0;
}