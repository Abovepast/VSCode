#include <iostream>
using namespace std;

const int N = 1e5+10;

int main() {

    double x = 0;
    string s = "";
    cin >> x >> s;

    if (s[0] == 'G') x=x*1024;
    if (s[0] == 'K') x=x/1024;
    if (s[0] == 'B') x=x/(1024*1024);

    for (int i = 2; i < 4; i++)
    {
        if (s[i] == '?')
        {
            if(s[i+1] == 'G') x=x/1024;
            if(s[i+1] == 'K') x=x*1024;
            if(s[i+1] == 'B') x=x*1024*1024;

            printf("%.6lf", x);
        }
    }

    return 0;
}