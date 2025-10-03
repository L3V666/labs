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

int patrition(int* a, int l, int r) {
    int x = a[r];
    int less = l;
    for (int i = l; i < r; i++) {
        if (a[i] <= x) {
            swap(a[i], a[less]);
            less++;
        }
    }
    swap(a[less], a[r]);
    return less;
}

void quick_sort(int* a, int l, int r) {
    if (l < r) {
        int q = patrition(a, l, r);
        quick_sort(a, l, q - 1);
        quick_sort(a, q + 1, r);
    }
}

signed main() {
    ofstream f("quick_sort_csv.csv", ios::out);
    for (int n = 100; n <= 50000; n += 100) {
        int a[n];
        for (int i = 0; i < n; i++) {
            a[i] = rand_uns(0, 999);
        }
        auto s = get_time();
        quick_sort(a, 0, n - 1);
        auto e = get_time();
        if (n == 100) {
            for (auto x : a) {
                cout << x << " ";
            }
        }
        f << n << "," << e - s << endl;
    }
}