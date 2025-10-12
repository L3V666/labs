#include <iostream>
#include <chrono>
#include <random>
#include <fstream>

using namespace std;

int rand_uns(int min, int max) {
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}

double get_time() {
    return std::chrono::duration_cast<std::chrono::microseconds>
        (std::chrono::steady_clock::now().time_since_epoch()).count()/1e6;
}

signed main() {
    ofstream f("-O1.csv", ios::out);
    for (int n = 2000; n <= 50000; n += 2000) {
        int a[n];
        for (int i = 0; i < n; i++) {
            a[i] = rand_uns(0, 999);
        }
        auto s = get_time();
        for (int i = 0; i + 1 < n; i++) {
            for (int j = 0; j + 1 < n - i; j++) {
                if (a[j + 1] < a[j]) {
                    swap(a[j], a[j + 1]);
                }
            }
        }
        auto e = get_time();
        f << n << "," << e - s << endl;
    }
}