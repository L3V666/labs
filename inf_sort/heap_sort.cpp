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

void heapify(int arr[], int n, int i) {
    int largest = i;   
    int l = 2*i + 1; 
    int r = 2*i + 2; 
    if (l < n && arr[l] > arr[largest])
        largest = l;
    if (r < n && arr[r] > arr[largest])
        largest = r;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    for (int i=n-1; i>=0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

signed main() {
    ofstream f("heap_sort_csv.csv", ios::out);
    for (int n = 4000; n <= 100000; n += 100) {
        int a[n];
        for (int i = 0; i < n; i++) {
            a[i] = rand_uns(0, 999);
        }
        auto s1 = get_time();
        heapSort(a, n);
        auto e1 = get_time();

        for (int i = 0; i < n; i++) {
            a[i] = i;
        }
        auto s2 = get_time();
        heapSort(a, n);
        auto e2 = get_time();

        for (int i = 0; i < n; i++) {
            a[i] = n - i;
        }
        auto s3 = get_time();
        heapSort(a, n);
        auto e3 = get_time();

        f << n << "," << e1 - s1 << "," << e2 - s2 << "," << e3 - s3 << endl;
    }
}