#include <iostream>
#include <chrono>
#include <random>
using namespace std;
int rand_uns(int min, int max) {
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}
signed main() {
    for (int i = 0; i < 10; i++) {
        cout << rand_uns(100, 200) << endl;

    }
}