#include <fstream>
#include <iostream>
#include <vector>

int main() {
    std::ofstream file("0.csv");

    if (!file.is_open()) {
        std::cerr << "Failed to open file\n";
        return 1;
    }

    long long n = 10000;  // кол-во итераций
    // std::cin >> n;

    std::vector<long long> a;  // контейнер на котором будем проверять

    file << 0 << "," << a.size() << "," << a.capacity() << "\n";

    for (int i = 0; i < n; i++) {
        a.push_back(8);
        file << i << "," << a.size() << "," << a.capacity() << "\n";
    }

    return 0;
}
