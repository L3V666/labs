#include <iostream>

using namespace std;

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

signed main() {
    subforwardlist list;
    list.push_back(13);
    cout << list.pop_back() << endl;
}