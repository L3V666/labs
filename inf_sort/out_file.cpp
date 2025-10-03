#include <fstream>
using namespace std;
int main()
{
    ofstream f("1.csv", ios::out);
    // csv - стандартный формат для хранения данных прямым текстом.
    f << "uno uno uno dos quatro" << endl; // работаете как с привычным cout
    return 0;
}
