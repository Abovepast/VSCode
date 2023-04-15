#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long LL;
const int N=1e6+10;

int k=0;
string str;

void dfs() {

    if(str[k]=='#') {
        k++;
        return;
    }

    char r = str[k++];

    dfs();
    cout<<r<<" ";
    dfs();

}

int main() {
    
    cin>>str;

    dfs();
    
    return 0;
}