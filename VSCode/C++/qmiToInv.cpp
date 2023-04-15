#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long LL;

//a%bµÄÄæÔª == a^(b-2)%b

LL qmi(LL a,LL p) {
    LL res =1;
    LL b=p-2;

    while(b!=0) {
        if((b&1)==1) {
            res=(res*a)%p;
        }
            b>>=1;
            a=a*a%p;
    }
    
    return res;
}

int main() {
    
    int n;
    cin>>n;

    while(n--) {
        int a,p;
        cin>>a>>p;
        if(a%p==0) cout<<"impossible"<<endl;
            else cout<<qmi(a,p)<<endl;
    }
    
    return 0;
}