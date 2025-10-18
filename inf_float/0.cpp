#include <iostream>

using namespace std;

void ui_to_bin(unsigned int a) {
    for (int i = 32 - 1; i >= 0; i--) {
        cout << ((a >> i) & 1);
        if (i != 0 && i % 8 == 0) {
            cout << " ";
        }
    }
}

signed main() {
    //4294967295
    unsigned int a;
    cin >> a;
    ui_to_bin(a);
}