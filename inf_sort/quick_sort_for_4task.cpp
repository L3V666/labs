#include <iostream>
#include <chrono>
#include <random>
#include <fstream>
#include <vector>

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
    int i = l - 1;
    for (int j = l; j < r; j++) {
        if (a[j] < x) {
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i + 1], a[r]);
    return i + 1;
}

void quick_sort(int* a, int l, int r) {
    if (l < r) {
        int q = patrition(a, l, r);
        quick_sort(a, l, q - 1);
        quick_sort(a, q + 1, r);
    }
}

signed main() {
    ofstream f("quick_sort_for_4task_csv.csv", ios::out);
    for (int n = 1000; n <= 30000; n += 100) {
        int a[n];

        for (int i = 0; i < n; i++) {
            a[i] = rand_uns(0, 999);
        }
        auto s1 = get_time();
        quick_sort(a, 0, n - 1);
        auto e1 = get_time();
        
        for (int i = 0; i < n; i++) {
            a[i] = i;
        }
        auto s2 = get_time();
        quick_sort(a, 0, n - 1);
        auto e2 = get_time();

        for (int i = 0; i < n; i++) {
            a[i] = n - i;
        }
        auto s3 = get_time();
        quick_sort(a, 0, n - 1);
        auto e3 = get_time();

        f << n << "," << e1 - s1 << "," << e2 - s2 << "," << e3 - s3 << endl;
    }
}