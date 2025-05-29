#include <stdlib.h>
#include <stdio.h>

int compare (const void *p_a, const void *p_b) {
    int *p_a_i = (int *) p_a;
    int *p_b_i = (int *) p_b;
    return *p_a_i-*p_b_i;
    }
int matrixSum(int** nums, int numsSize, int* numsColSize) {
    // sort each subarray
    for (int i = 0; i < numsSize; ++i) {
        qsort(*nums[i], numsSize, sizeof(int), compare);
    }
    // print
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 3; ++j) {
            printf("%d ", (**nums)[i][j] );
        }
    }
}

int main () {
    int yay[4][3] = {{7,2,1},{6,4,2},{6,5,3},{3,2,1}};

    return 0;
}