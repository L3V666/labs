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

void merge(int* a, int l, int m, int r) {
    int n1 = m - l + 1;  
    int n2 = r - m;
    int L[n1], R[n2];
    for (int i = 0; i < n1; ++i)
        L[i] = a[l + i];
    for (int j = 0; j < n2; ++j)
        R[j] = a[m + 1 + j];

    int i = 0, j = 0, k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            a[k++] = L[i++];
        else
            a[k++] = R[j++];
    }

    // Добавляем оставшиеся элементы
    while (i < n1)
        a[k++] = L[i++];
    while (j < n2)
        a[k++] = R[j++];
}

void merge_sort(int* a, int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    merge_sort(a, l, m);
    merge_sort(a, m + 1, r);
    merge(a, l, m, r);
}


signed main() {
    ofstream f("merge_sort_csv.csv", ios::out);
    for (int n = 4000; n <= 100000; n += 100) {
        int a[n];
        for (int i = 0; i < n; i++) {
            a[i] = rand_uns(0, 999);
        }
        auto s1 = get_time();
        merge_sort(a, 0, n - 1);
        auto e1 = get_time();

        for (int i = 0; i < n; i++) {
            a[i] = i;
        }
        auto s2 = get_time();
        merge_sort(a, 0, n - 1);
        auto e2 = get_time();

        for (int i = 0; i < n; i++) {
            a[i] = n - i;
        }
        auto s3 = get_time();
        merge_sort(a, 0, n - 1);
        auto e3 = get_time();

        f << n << "," << e1 - s1 << "," << e2 - s2 << "," << e3 - s3 << endl;
    }
}