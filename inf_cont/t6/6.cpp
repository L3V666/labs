#include <chrono>
#include <forward_list>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <vector>

volatile long long guard = 0;

template <typename Container>
long long traverse_container(const Container& c) {
    long long sum = 0;

    for (const auto& x : c) {
        sum += static_cast<long long>(x) + 1;
    }

    return sum;
}

long long traverse_map(const std::map<int, int>& mp) {
    long long sum = 0;

    for (const auto& p : mp) {
        sum += static_cast<long long>(p.first) + p.second + 1;
    }

    return sum;
}

template <typename Function>
long long measure_time(Function func, int k) {
    long long total_time = 0;

    for (int j = 0; j < k; j++) {
        auto start = std::chrono::steady_clock::now();

        long long result = func();

        auto end = std::chrono::steady_clock::now();

        guard += result;

        auto duration =
            std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);

        total_time += duration.count();
    }

    return total_time / k;
}

int main() {
    std::ofstream file("6.csv");

    if (!file.is_open()) {
        std::cerr << "Ошибка открытия файла\n";
        return 1;
    }

    const int n = 3000000;  // максимальный размер контейнера
    const int k = 100;      // количество повторов для одного размера
    int step = 50000;

    std::vector<int> v;
    std::forward_list<int> flst;
    std::list<int> lst;
    std::map<int, int> mp;
    std::set<int> st;

    v.reserve(n);

    file << "size,vector,forward_list,list,map,set\n";

    for (int size = step; size <= n; size += step) {
        while (static_cast<int>(v.size()) < size) {
            int x = static_cast<int>(v.size()) + 1;

            v.push_back(x);
            flst.push_front(x);
            lst.push_back(x);
            mp.emplace(x, x);
            st.insert(x);
        }

        long long d_vector =
            measure_time([&]() { return traverse_container(v); }, k);

        long long d_forward_list =
            measure_time([&]() { return traverse_container(flst); }, k);

        long long d_list =
            measure_time([&]() { return traverse_container(lst); }, k);

        long long d_map = measure_time([&]() { return traverse_map(mp); }, k);

        long long d_set =
            measure_time([&]() { return traverse_container(st); }, k);

        file << size << "," << d_vector << "," << d_forward_list << ","
             << d_list << "," << d_map << "," << d_set << "\n";

        if (size % 100000 == 0) {
            std::cout << size << std::endl;
        }
    }

    file.close();

    return 0;
}