#include <iostream>

using namespace std;

signed main() {
    cout << fixed;
    cout.precision(1);
    for (float i = (1 << 24) - 1000; i < (1 << 24) + 2; i++) {
        cout << i << endl;
    }
}