#include "iostream"
#include "cmath"

typedef long long LL;
using namespace std;

LL n = 202320232023;

int main() {

    LL sum =1;
    LL num =0;
    
    const int cn = 1000000000;
    n%=cn;

    for (LL i = 1; i <= n; i++)
    {
        sum= (sum*i)%cn;
        num= (num+sum)%cn;
    }  
    
    cout<<"num = "<<num<<endl;
    //cout<<"sum = "<<sum<<endl;

    return 0;
}