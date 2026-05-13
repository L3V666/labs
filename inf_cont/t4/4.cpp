#include <chrono>
#include <cstddef>
#include <forward_list>
#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <utility>

class subforwardlist {
   private:
    struct Node {
        int data;
        Node* next;

        Node(int d) : data(d), next(nullptr) {}
    };

    Node* head;
    Node* tail;
    unsigned int sz;

    void clear() {
        Node* cur = head;

        while (cur) {
            Node* next = cur->next;
            delete cur;
            cur = next;
        }

        head = nullptr;
        tail = nullptr;
        sz = 0;
    }

    void copy_from(const subforwardlist& other) {
        head = nullptr;
        tail = nullptr;
        sz = 0;

        Node* cur = other.head;

        while (cur) {
            push_back(cur->data);
            cur = cur->next;
        }
    }

   public:
    subforwardlist();

    subforwardlist(const subforwardlist& other);

    subforwardlist& operator=(const subforwardlist& other);

    ~subforwardlist();

    void push_back(int d);

    int pop_back();

    void push_forward(int d);

    int pop_forward();

    unsigned int size() const;

    void push_where(int where, int d);

    int erase_where(int where);
};

subforwardlist::subforwardlist() : head(nullptr), tail(nullptr), sz(0) {}

subforwardlist::subforwardlist(const subforwardlist& other)
    : head(nullptr), tail(nullptr), sz(0) {
    copy_from(other);
}

subforwardlist& subforwardlist::operator=(const subforwardlist& other) {
    if (this != &other) {
        subforwardlist temp(other);

        std::swap(head, temp.head);
        std::swap(tail, temp.tail);
        std::swap(sz, temp.sz);
    }

    return *this;
}

subforwardlist::~subforwardlist() { clear(); }

void subforwardlist::push_back(int d) {
    Node* node = new Node(d);

    if (head == nullptr) {
        head = node;
        tail = node;
    } else {
        tail->next = node;
        tail = node;
    }

    sz++;
}

int subforwardlist::pop_back() {
    if (head == nullptr) {
        return 0;
    }

    if (head == tail) {
        int val = head->data;

        delete head;

        head = nullptr;
        tail = nullptr;
        sz = 0;

        return val;
    }

    Node* cur = head;

    while (cur->next != tail) {
        cur = cur->next;
    }

    int val = tail->data;

    delete tail;

    tail = cur;
    tail->next = nullptr;

    sz--;

    return val;
}

void subforwardlist::push_forward(int d) {
    Node* node = new Node(d);

    node->next = head;
    head = node;

    if (tail == nullptr) {
        tail = node;
    }

    sz++;
}

int subforwardlist::pop_forward() {
    if (head == nullptr) {
        return 0;
    }

    Node* node = head;
    int val = node->data;

    head = head->next;

    if (head == nullptr) {
        tail = nullptr;
    }

    delete node;

    sz--;

    return val;
}

unsigned int subforwardlist::size() const { return sz; }

void subforwardlist::push_where(int where, int d) {
    if (where <= 0 || head == nullptr) {
        push_forward(d);
        return;
    }

    if (static_cast<unsigned int>(where) >= sz) {
        push_back(d);
        return;
    }

    Node* cur = head;

    for (int i = 0; i + 1 < where; i++) {
        cur = cur->next;
    }

    Node* node = new Node(d);

    node->next = cur->next;
    cur->next = node;

    sz++;
}

int subforwardlist::erase_where(int where) {
    if (head == nullptr) {
        return 0;
    }

    if (where <= 0) {
        return pop_forward();
    }

    if (static_cast<unsigned int>(where) >= sz - 1) {
        return pop_back();
    }

    Node* prev = head;

    for (int i = 0; i + 1 < where; i++) {
        prev = prev->next;
    }

    Node* cur = prev->next;
    int val = cur->data;

    prev->next = cur->next;

    delete cur;

    sz--;

    return val;
}

int main() {
    std::ofstream file("4.csv");

    if (!file.is_open()) {
        std::cerr << "Ошибка открытия файла\n";
        return 1;
    }

    const int k = 1000;     // количество повторов для одного размера
    const int n = 3000000;  // максимальный размер списка
    int step = 1000;

    std::list<int> lst;
    std::forward_list<int> flst;
    subforwardlist slst;

    int lst_size = 0;
    int flst_size = 0;

    file << "size,list,forward_list,subforwardlist\n";

    for (int i = step; i < n; i += step) {
        while (lst_size < i) {
            lst.push_front(8);
            lst_size++;
        }

        while (flst_size < i) {
            flst.push_front(8);
            flst_size++;
        }

        while (slst.size() < static_cast<unsigned int>(i)) {
            slst.push_forward(8);
        }

        long long d_lst = 0;

        for (int j = 0; j < k; j++) {
            auto start = std::chrono::steady_clock::now();

            int value = lst.front();
            lst.pop_front();

            auto end = std::chrono::steady_clock::now();

            lst.push_front(value);

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_lst += duration.count();
        }

        long long d_flst = 0;

        for (int j = 0; j < k; j++) {
            int value = flst.front();

            auto start = std::chrono::steady_clock::now();

            flst.pop_front();

            auto end = std::chrono::steady_clock::now();

            flst.push_front(value);

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_flst += duration.count();
        }

        long long d_slst = 0;

        for (int j = 0; j < k; j++) {
            auto start = std::chrono::steady_clock::now();

            int value = slst.pop_forward();

            auto end = std::chrono::steady_clock::now();

            slst.push_forward(value);

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_slst += duration.count();
        }

        file << i << "," << d_lst / k << "," << d_flst / k << "," << d_slst / k
             << "\n";

        if (i % 100000 == 0) {
            std::cout << i << std::endl;
        }
    }

    file.close();

    return 0;
}