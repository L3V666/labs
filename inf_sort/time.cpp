#include <iostream>
#include <chrono>


double get_time() {
    return std::chrono::duration_cast<std::chrono::microseconds>
        (std::chrono::steady_clock::now().time_since_epoch()).count()/1e6;
}

int main() {
    
    return 0;
}