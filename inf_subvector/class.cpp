#include <iostream>

using namespace std;

class subvector {
   public:
    subvector();

    ~subvector();

    void push_back(int d);

    void pop_back();

    void clear();

    int& operator[](unsigned int i);

    unsigned int size();

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

void subvector::clear() { top = 0; }

int& subvector::operator[](unsigned int i) { return mas[i]; }

unsigned int subvector::size() { return top; }

signed main() {
    subvector a;
    a.push_back(2);
    cout << a[0] << endl;
    cout << a.size();
    return 0;
}