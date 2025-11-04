#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

#define e (double)0.0000001
#define E (double)1000000

signed main() {
    //y = x
    ofstream fd("4_double.csv", ios::out);
    // for (double step = 0.00001; step > e; step -= e) {
    //     float c = 0;
    //     for (double i = step; i <= 1.0; i += step) {
    //         c += ((i - 0.5 * step) * step);
    //     }
    //     fd << E - step * E << "," << c << endl;
    // }


    double s;
    double one=1.0;
    double x;
    long long i;
    for (long long number_of_rects = 1; number_of_rects < 4294967296 && number_of_rects * 2 > number_of_rects; number_of_rects *= 2){
        x = 0;
        s = 10000000;
        i = 0;
        while (i < number_of_rects) {
            s += ((one / (number_of_rects)) * i) * (one / number_of_rects);
            i++;
        }
        fd << number_of_rects << ',' << s-10000000 << '\n';
    }
    system("4.py");
}