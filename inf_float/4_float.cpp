#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

#define unsigned long long

#define e (double)0.0000001
#define E (double)1000000

signed main() {
    //y = x
    ofstream ff("4_float.csv", ios::out);
    for (float step = 0.001; step > e; step -= e) {
        float c = 0;
        for (float i = step; i <= 1.0; i += step) {
            c += ((i - 0.5 * step) * step);
        }
        ff << E - step * E << "," << c << endl;
    }
    system("4.py");
}