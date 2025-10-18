#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

#define long double double
#define unsigned long long

#define e (double)0.0000001
#define E (double)1000000

signed main() {
    //y = x
    ofstream ff("4_float.csv", ios::out);
    // ff << fixed;
    // ff.precision(5);
    for (double step = 0.001; step > e; step -= e) {
        float c = 0;
        for (double i = step; i <= 1.0; i += step) {
            c += ((i - 0.5 * step) * step);
        }
        ff << E - step * E << "," << c << endl;
    }
    ofstream fd("4_double.csv", ios::out);
    // fd << fixed;
    // fd.precision(5);
    for (double step = 0.001; step > e; step -= e) {
        double c = 0;
        for (double i = step; i <= 1.0; i += step) {
            c += ((i - 0.5 * step) * step);
        }
        fd << E - step * E << "," << c << "," << step << endl;
    }
    system("4.py");
}