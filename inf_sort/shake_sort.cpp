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
    ofstream f("shake_sort_csv.csv", ios::out);
    for (int n = 100; n <= 50000; n += 100) {
        int a[n];
        for (int i = 0; i < n; i++) {
            a[i] = rand_uns(0, 999);
        }
        auto s = get_time();
        int l = 0;
        int r = n - 1;
        while (l <= r) {
            for (int i = r; i > l; i--) {
                if (a[i - 1] > a[i]) {
                    swap(a[i - 1], a[i]);
                }
            }
            l++;
            for (int i = l; i < r; i++) {
                if (a[i] > a[i + 1]) {
                    swap(a[i], a[i + 1]);
                }
            }
            r--;
        }
        auto e = get_time();
        f << n << "," << e - s << endl;
    }
}