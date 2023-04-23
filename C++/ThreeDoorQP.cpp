#include <iostream>
#include <time.h>

using namespace std;

int main() {
    
    int n=100000,n1=n;
    int i=0,j=0,k=0;
    int change=0,notChange=0;

    srand((unsigned)time(NULL));
    i=rand()%3+1;//取一个1-3的随机数作为答案

    //不换门
    while(n--) {
        j=rand()%3+1;//取一个随机数作为选择
        if(j==i) notChange++;
    }

    //换门
    while(n1--) {
        j=rand()%3+1;   //你选择一扇门

        k=rand()%3+1;   //主持人打开的那扇门
        while(k==j || k==i) k=rand()%3+1;   //当然k不会是有车的门（k!=i）,也不会是你开始选的门（k!=j）

        int j0=j;
        while(j==k || j==j0) j=rand()%3+1;  //你换的门不是你开始选的门（j!=j0）,也不是主持人已经打开的门（j!=k）

        if(j==i) change++;
    }

    cout<<"notChange = "<<notChange<<endl;
    cout<<"change = "<<change<<endl;
    
    return 0;
}