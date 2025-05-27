#include <stdlib.h>

// Create an array of n integers and fill it with values 0 to n-1
int* make_array(int n) {
    int* arr = (int*) malloc(n * sizeof(int));
    if (!arr) return NULL;

    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }

    return arr;
}
