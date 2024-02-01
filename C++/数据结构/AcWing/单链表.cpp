# include <iostream>
using namespace std;
const int N = 100010;

int head, e[N], ne[N], idx;

void init() {
    head = -1;
    idx = 0;
}

// 在头结点后插入一个数
int add_to_head(int x) {
    e[idx] = x, ne[idx] = head, head = idx, idx ++;
}

// 在第k个插入的数后插入一个数
int add(int k, int x) {
    e[idx] = x, ne[idx] = ne[k], ne[k] = idx, idx ++;
}

// 删除第k个插入的数后面一个数
void del(int k) {
    ne[k] = ne[ne[k]];
}

int main () {

    init();

    int m;
    cin >> m;

    while(m--) {
        int k, x;
        char op;

        cin >> op;
        if (op == 'H') {
            cin >> x;
            add_to_head(x);
        } else if (op == 'D') {
            cin >> k;
            if (!k) head = ne[head];    // 特判：删除头结点
            del(k-1);
        } else if (op == 'I') {
            cin >> k >> x;
            add(k-1, x);
        }
    }

    for (int i = head; i != -1; i = ne[i]) cout << e[i] <<' ';
    cout << endl;
    return 0;
}
