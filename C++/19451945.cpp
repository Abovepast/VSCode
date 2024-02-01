/**
 * 
 * 找出x^2 + y^2 = 19451945的解集
 * 
*/
# include <iostream>
# include <cmath>

using namespace std;
const int N = 1e6+10;

int NUM = 19451945;
int sNum = sqrt((double)NUM) + 1;

int main() {

    for (int x = 1;x<sNum;x++)
        for (int y = 1;y<x;y++)
            if(x*x + y*y == NUM) {
                printf("%-4d %-4d\n", x, y);
            }

    return 0;
}