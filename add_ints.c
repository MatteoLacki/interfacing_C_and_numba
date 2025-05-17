#include <stdint.h>

int64_t sum(int64_t a, int64_t b){
   return a + b;
}

// gcc add_ints.c -fPIC -shared -o add_ints.so