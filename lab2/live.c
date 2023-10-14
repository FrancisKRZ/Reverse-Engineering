#include <stdio.h>
#include <stdlib.h>

int iAmGlobalVar = 55;
int iAmUninit[100] ;

int foo(int a) {
    int g = 90 * a;
    static int iAmStatic;
    printf("stack in foo %p\n", &g);
    return 0;
}

int main() {
    int x = 42;

    printf("Hello world\n");
    printf("stack %p\n", &x);
    x = foo(0);

    int *m = malloc(10000);
    printf("heap 0: %p\n", m);

    int *n = malloc(10000);
    printf("heap 1 : %p\n", n);

    printf("foo\'s address: %p\n", foo );
    while(1);

    return 0;
}
