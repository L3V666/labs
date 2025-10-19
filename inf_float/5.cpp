#include <iostream>
#include <iomanip>
#include <cstdint>
#include <cstring>
#include <cmath>
#include <xmmintrin.h>   // _mm_getcsr/_mm_setcsr
#include <cfloat>        // FLT_MIN

void print_float_bits(const char* label, float v) {
    uint32_t u;
    std::memcpy(&u, &v, sizeof(u));
    std::cout << label << ": value=" << std::setprecision(9) << v
              << ", hex=0x" << std::hex << u << std::dec << "\n";
}

int main() {
    //_mm_setcsr(_mm_getcsr() | 0x8040);
    _mm_setcsr(_mm_getcsr() & ~0x8040);
    // 1) самый простой способ получить значение ниже FLT_MIN:
    volatile float a = FLT_MIN;           // наименьшее нормальное
    volatile float b = 0.5f;             // делитель -> результат < FLT_MIN (денормаль)
    volatile float r = a * b;            // может стать denormal (или 0, если FTZ включён)

    // 2) альтернативный способ — ближайшее представимое к FLT_MIN по направлению к 0
    float den_via_next = nextafterf(FLT_MIN, 0.0f);

    // 3) печать
    print_float_bits("FLT_MIN", FLT_MIN);
    print_float_bits("den (nextafter)", den_via_next);
    print_float_bits("result a*b", r);

    // 4) показать MXCSR bits (FTZ bit15, DAZ bit6)
    unsigned int mx = _mm_getcsr();
    std::cout << "MXCSR = 0x" << std::hex << mx << std::dec
              << " (FTZ=" << ((mx>>15)&1) << ", DAZ=" << ((mx>>6)&1) << ")\n";

    return 0;
}