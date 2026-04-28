#include <chrono>
#include <fstream>
#include <iostream>
#include <random>
#include <vector>

class subvector {
   public:
    subvector();

    ~subvector();

    void push_back(int d);

    void pop_back();

    void clear();

    void insert(unsigned int pos, int value);

    void erase(unsigned int pos);

    int& operator[](unsigned int i);

    unsigned int size();

    subvector(const subvector& other);

    subvector& operator=(const subvector& other) {
        if (this == &other) return *this;

        delete[] mas;

        top = other.top;
        capacity = other.capacity;
        mas = new int[capacity];

        for (unsigned int i = 0; i < top; i++) {
            mas[i] = other.mas[i];
        }

        return *this;
    }

   private:
    unsigned int top;
    unsigned int capacity;
    int* mas;
};

subvector::subvector() {
    top = 0;
    capacity = 0;
    mas = nullptr;
}

subvector::subvector(const subvector& other) {
    top = other.top;
    capacity = other.capacity;
    mas = new int[capacity];

    for (unsigned int i = 0; i < top; i++) {
        mas[i] = other.mas[i];
    }
}

subvector::~subvector() {
    delete[] mas;
    mas = nullptr;
    top = 0;
    capacity = 0;
}

void subvector::push_back(int d) {
    if (top == capacity) {
        int* t = new int[capacity * 2 + 1];
        capacity *= 2;
        capacity++;
        for (unsigned int i = 0; i < top; i++) {
            t[i] = mas[i];
        }
        delete[] mas;
        mas = t;
    }
    mas[top++] = d;
}

void subvector::pop_back() {
    if (top == 0) return;
    top--;
}

void subvector::insert(unsigned int pos, int value) {
    if (pos > top) return;

    if (top == capacity) {
        int new_capacity = capacity * 2 + 1;
        int* t = new int[new_capacity];

        for (unsigned int i = 0; i < pos; ++i) {
            t[i] = mas[i];
        }

        t[pos] = value;

        for (unsigned int i = pos; i < top; ++i) {
            t[i + 1] = mas[i];
        }

        delete[] mas;
        mas = t;
        capacity = new_capacity;
    } else {
        for (unsigned int i = top; i > pos; --i) {
            mas[i] = mas[i - 1];
        }
        mas[pos] = value;
    }

    top++;
}

void subvector::erase(unsigned int pos) {
    if (pos >= top) return;

    for (unsigned int i = pos; i + 1 < top; ++i) {
        mas[i] = mas[i + 1];
    }

    --top;
}

void subvector::clear() { top = 0; }

int& subvector::operator[](unsigned int i) { return mas[i]; }

unsigned int subvector::size() { return top; }

int main() {
    std::mt19937 gen(std::random_device{}());  // генератор

    std::ofstream file("2.csv");

    int k = 100;    // кол-во вставок элементов при одной длине массива
    int n = 10000;  // макс размер массива
    // std::cin >> n;

    std::vector<int> v;
    subvector sv;

    for (int i = 1; i < n; i++) {
        // добить вектор до нужного размера
        while (v.size() < i) v.push_back(8);
        while (sv.size() < i) sv.push_back(8);

        int s = v.size();

        long long d_v = 0;

        for (int j = 0; j < k; j++) {
            auto t_v = v;

            std::uniform_int_distribution<int> dist(0,
                                                    s - 1);  // диапазон [l, r]
            int x = dist(gen);

            auto start = std::chrono::steady_clock::now();

            t_v.erase(t_v.begin() + x);

            auto end = std::chrono::steady_clock::now();

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_v += duration.count();
        }

        s = sv.size();

        long long d_sv = 0;

        for (int j = 0; j < k; j++) {
            auto t_sv = sv;

            std::uniform_int_distribution<int> dist(0,
                                                    s - 1);  // диапазон [l, r]
            int x = dist(gen);

            auto start = std::chrono::steady_clock::now();

            t_sv.erase(x);

            auto end = std::chrono::steady_clock::now();

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_sv += duration.count();
        }

        file << i << "," << d_v / k << "," << d_sv / k << "\n";
    }
}