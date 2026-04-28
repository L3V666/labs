#include <chrono>
#include <fstream>
#include <forward_list>
#include <iostream>
#include <list>
#include <random>

class subforwardlist {
   private:
    struct Node {
        int data;
        Node* next;
        Node(int d) : data(d), next(nullptr) {}
    };

    Node* head;

   public:
    subforwardlist();

    ~subforwardlist();

    void push_back(int d);

    int pop_back();

    void push_forward(int d);

    int pop_forward();

    unsigned int size();

    void push_where(unsigned int where, int d);

    int erase_where(unsigned int where);
};

subforwardlist::subforwardlist() { head = nullptr; }

subforwardlist::~subforwardlist() {
    Node* cur = head;
    while (cur) {
        Node* next = cur->next;
        delete cur;
        cur = next;
    }
    head = nullptr;
}

void subforwardlist::push_back(int d) {
    Node* node = new Node(d);
    if (head == nullptr) {
        head = node;
        return;
    }
    Node* cur = head;
    while (cur->next) cur = cur->next;
    cur->next = node;
}

int subforwardlist::pop_back() {
    if (head == nullptr) return 0;
    if (head->next == nullptr) {
        int val = head->data;
        delete head;
        head = nullptr;
        return val;
    }
    Node* cur = head;
    Node* prev = nullptr;
    while (cur->next) {
        prev = cur;
        cur = cur->next;
    }
    int val = cur->data;
    delete cur;
    prev->next = nullptr;
    return val;
}

void subforwardlist::push_forward(int d) {
    Node* node = new Node(d);
    node->next = head;
    head = node;
}

int subforwardlist::pop_forward() {
    if (head == nullptr) return 0;
    Node* node = head;
    int val = node->data;
    head = node->next;
    delete node;
    return val;
}

unsigned int subforwardlist::size() {
    unsigned int cnt = 0;
    Node* cur = head;
    while (cur) {
        cnt++;
        cur = cur->next;
    }
    return cnt;
}

void subforwardlist::push_where(unsigned int where, int d) {
    if (where == 0 || head == nullptr) {
        push_forward(d);
    }
    if (where >= size()) {
    }
    Node* cur = head;
    unsigned int i = 0;
    while (cur->next && i + 1 < where) {
        cur = cur->next;
        i++;
    }
    Node* node = new Node(d);
    node->next = cur->next;
    cur->next = node;
}

int subforwardlist::erase_where(unsigned int where) {
    if (head == nullptr) return 0;
    if (where == 0) return pop_forward();
    if (where >= size() - 1) return pop_back();

    Node* cur = head;
    Node* prev = nullptr;
    unsigned int i = 0;
    while (cur && i < where) {
        prev = cur;
        cur = cur->next;
        i++;
    }
    if (!cur) return 0;

    int val = cur->data;
    prev->next = cur->next;
    delete cur;
    return val;
}

int main() {
    std::mt19937 gen(std::random_device{}());  // генератор

    std::ofstream file("3.csv");

    int k = 100;    // кол-во вставок элементов при одной длине массива
    int n = 10000;  // макс размер массива
    // std::cin >> n;

    std::list<int> lst;
    std::forward_list<int> flst;
    subforwardlist slst;

    

    for (int i = 1; i < n; i++) {
        // добить вектор до нужного размера
        while (lst.size() < i) lst.push_front(8);
        while (std::distance(flst.begin(), flst.end()) < i) flst.push_front(8);
        while (slst.size() < i) slst.push_forward(8);

        int s = lst.size();

        long long d_lst = 0;

        for (int j = 0; j < k; j++) {
            auto t_lst = lst;

            auto start = std::chrono::steady_clock::now();

            t_lst.push_front(8);

            auto end = std::chrono::steady_clock::now();

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_lst += duration.count();
        }

        s = std::distance(flst.begin(), flst.end());

        long long d_flst = 0;

        for (int j = 0; j < k; j++) {
            auto t_flst = flst;

            std::uniform_int_distribution<int> dist(0,
                                                    s - 1);  // диапазон [l, r]
            int x = dist(gen);

            auto start = std::chrono::steady_clock::now();

            t_flst.push_front(8);

            auto end = std::chrono::steady_clock::now();

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_flst += duration.count();
        }

        s = slst.size();

        long long d_slst = 0;

        for (int j = 0; j < k; j++) {
            auto t_slst = flst;

            auto start = std::chrono::steady_clock::now();

            t_slst.push_front(8);

            auto end = std::chrono::steady_clock::now();

            auto duration =
                std::chrono::duration_cast<std::chrono::nanoseconds>(end -
                                                                     start);

            d_slst += duration.count();
        }

        file << i << "," << d_lst / k << "," << d_flst / k << "," << d_slst << "\n";
    }
}