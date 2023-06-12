#include <iostream>
using namespace std;

int main() {

    double A[110]={0};

    for(int i = 0; i <100; i++) {
        cin>>A[i];
        if(A[i]<=10) printf("A[%d] = %.1lf\n",i, A[i]);
    } 

    return 0;
}