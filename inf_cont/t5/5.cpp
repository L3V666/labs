#include <chrono>
#include <fstream>
#include <iostream>
#include <map>
#include <random>
#include <set>
#include <utility>

int main() {
    std::mt19937 gen(std::random_device{}());
    std::uniform_int_distribution<int> dist(1, 1000);

    std::ofstream file("5.csv");

    if (!file.is_open()) {
        std::cerr << "Ошибка открытия файла\n";
        return 1;
    }

    const int k = 1000;     // количество повторов для одного размера
    const int n = 3000000;  // максимальный размер списка
    int step = 1000;

    std::set<int> st = {0};
    std::map<int, int> mp;
    mp[0] = 0;
    std::multiset<int> mst = {0};
    std::multimap<int, int> mmp = {{0, 0}};

    file << "size,set,map,multiset,multimap\n";

    for (int i = step; i < n; i += step) {
        while (static_cast<int>(st.size()) < i) {
            st.insert(*st.rbegin() + 1);
        }

        while (static_cast<int>(mst.size()) < i) {
            mst.insert(*mst.rbegin() + 1);
        }

        while (static_cast<int>(mp.size()) < i) {
            int key = mp.rbegin()->first + 1;
            mp[key] = key;
        }

        while (static_cast<int>(mmp.size()) < i) {
            int key = mmp.rbegin()->first + 1;
            mmp.insert({key, key});
        }

        int x = i;
        int y = dist(gen);

        long long d_st = 0;

        for (int j = 0; j < k; j++) {
            auto start = std::chrono::steady_clock::now();

            st.insert(x);

            auto end = std::chrono::steady_clock::now();

            st.erase(x);

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_st += duration.count();
        }

        long long d_mp = 0;

        for (int j = 0; j < k; j++) {
            auto start = std::chrono::steady_clock::now();

            mp[x] = y;

            auto end = std::chrono::steady_clock::now();

            mp.erase(x);

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_mp += duration.count();
        }

        long long d_mst = 0;

        for (int j = 0; j < k; j++) {
            auto start = std::chrono::steady_clock::now();

            mst.insert(x);

            auto end = std::chrono::steady_clock::now();

            mst.erase(x);

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_mst += duration.count();
        }

        long long d_mmp = 0;

        for (int j = 0; j < k; j++) {
            auto start = std::chrono::steady_clock::now();

            mmp.insert({x, y});

            auto end = std::chrono::steady_clock::now();

            mmp.erase(x);

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_mmp += duration.count();
        }

        file << i << "," << d_st / k << "," << d_mp / k << "," << d_mst / k
             << "," << d_mmp / k << "\n";

        if (i % 100000 == 0) {
            std::cout << i << std::endl;
        }
    }

    file.close();

    return 0;
}