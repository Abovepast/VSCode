#include <iostream>
using namespace std;
const int N=1e6+10;
typedef long long LL;

int q[N],sum;

void quick_sort(int q[], int l, int r) {
    if(l>=r) return;
    int x=q[(l+r)>>1], i=l-1, j=r+1;

    while(i<j) {
        do i++;while(q[i]<x);
        do j--;while(q[j]>x);
        if(i<j) swap(q[i], q[j]);
    }

    quick_sort(q, l, j), quick_sort(q, j+1, r);
}

// void select_num(LL x) {
    
// }

int main() {
    bool flag=true;

    // for(LL x=1;x<20;x++) {

    LL x;
    cin>>x;

        //找公约数（去除自身），保存在q[]
        int k = 0;
        sum=0;
        for(int i=1,k=0;i*i<=x;i++) {
            if(x%i==0) {
                if (i < x) q[k++] = i,sum+= i;
                if (x / i < x) q[k++] = x / i,sum+= x/i;  //加上'='就可以加上自身x
            }
        }
        
        //排序
        quick_sort(q, 0, k-1);

        for(int i=0;i<k;i++) cout<<q[i]<<" ";

        //对q[]进行筛选
        // select_num(x);
        // for(int i=0;i<k;i++) {
        //     if((q[i]+sum)==x) {

        //         for(int i=0;i<k;i++) cout<<q[i]<<' ';
        //         cout<<endl;
        //         cout<<q[i]<<"+"<<sum<<"=="<<q[i]+sum<<"----"<<x<<endl;
        //         cout<<"x = "<<x<<endl;
        //         flag=false;
        //     }
        // }
    // }
}