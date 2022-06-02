#include <stdio.h>

typedef int (*t_somefunc)(int, int);

int product(int u, int v) {
    return u * v;
}

int main(int argc, char const *argv[]) {
    t_somefunc afunc = &product;
    printf("%d\n", (*afunc)(123, 456));
    return 0;
}
