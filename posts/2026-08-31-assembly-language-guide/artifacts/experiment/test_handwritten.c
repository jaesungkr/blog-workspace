#include <stdio.h>

int asm_add(int a, int b);

int main(void) {
    const int cases[][2] = {
        {7, 5},
        {-4, 9},
        {1000000, 234567},
    };

    for (unsigned long i = 0; i < sizeof(cases) / sizeof(cases[0]); ++i) {
        const int a = cases[i][0];
        const int b = cases[i][1];
        printf("asm_add(%d, %d) = %d\n", a, b, asm_add(a, b));
    }
    return 0;
}
