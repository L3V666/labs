#include <fstream>
#include <iostream>
#include <vector>

int main() {
    std::ofstream file("0.csv");

    if (!file.is_open()) {
        std::cerr << "Failed to open file\n";
        return 1;
    }

    int n = 3000000;  // кол-во итераций
    int step = 10000;

    std::vector<long long> a;  // контейнер на котором будем проверять

    file << 0 << "," << a.size() << "," << a.capacity() << "\n";

    for (int i = step; i < n; i += step) {
        while (a.size() < i) a.push_back(8);
        file << i << "," << a.size() << "," << a.capacity() << "\n";

        if (i % 1000000 == 0) std::cout << i << std::endl;
    }

    return 0;
}
