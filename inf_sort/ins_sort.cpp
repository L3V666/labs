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
    ofstream f("ins_sort_csv.csv", ios::out);
    for (int n = 4000; n <= 100000; n += 4000) {
        int a[n];
        for (int i = 0; i < n; i++) {
            a[i] = rand_uns(0, 999);
        }
        auto s1 = get_time();
        for (int i = 1; i < n; i++) {
            int x = a[i];
            int j = i;
            while (j > 0 && a[j - 1] > x) {
                a[j] = a[j - 1];
                j--;
            }
            a[j] = x;
        }
        auto e1 = get_time();
        for (int i = 0; i < n; i++) {
            a[i] = i;
        }
        auto s2 = get_time();
        for (int i = 1; i < n; i++) {
            int x = a[i];
            int j = i;
            while (j > 0 && a[j - 1] > x) {
                a[j] = a[j - 1];
                j--;
            }
            a[j] = x;
        }
        auto e2 = get_time();
        for (int i = 0; i < n; i++) {
            a[i] = n - i;
        }
        auto s3 = get_time();
        for (int i = 1; i < n; i++) {
            int x = a[i];
            int j = i;
            while (j > 0 && a[j - 1] > x) {
                a[j] = a[j - 1];
                j--;
            }
            a[j] = x;
        }
        auto e3 = get_time();
        f << n << "," << e1 - s1 << "," << e2 - s2 << "," << e3 - s3 << endl;
    }
}