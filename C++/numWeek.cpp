#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long LL;
const int N=1e6+10;

LL qmi(LL a, LL b, LL mode) {

    a%=mode;
    b%=mode;
    LL sum=1;

    while (b) {
        //��ȡb��λ����
        if((b&1)==1) sum=(sum*a)%mode;
        //b����һλ
        b>>=1;
        //a��һ��
        a=(a*a)%mode;
    }

    return sum;
}

int main() {
    
    int curDay = 6;
    int gipDay = qmi(2020,2020,7);

    int endDay = (curDay+gipDay)%7;

    if(!endDay) endDay = 7;
    cout<<"��������"<<endDay<<endl;

    return 0;
}
