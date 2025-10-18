#include <iostream>

using namespace std;

union fu {
 float f;
 unsigned int u;
};

void ui_to_bin(unsigned int a) {
    for (int i = 32 - 1; i >= 0; i--) {
        cout << ((a >> i) & 1);
        if (i == 31 || i == 23) {
            cout << "|";
        }
        if (i != 0 && i % 4 == 0) {
            cout << " ";
        }
    }
}

signed main() {
    fu a;
    //137.375
    cin >> a.f;
    ui_to_bin(a.u);
}