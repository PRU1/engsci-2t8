// Find the minimum ways to get to a target sum from a collection of numbers
// use DP
#include <stdio.h>


int main () {
    int arr[] = {1,5,7};
    int target = 12;
    int *solSpace = malloc(sizeof(int)*(target+1));
    solSpace[0] = 0;
    // initialize empty, see if there's a better way to do this
    for (int i = 1; i < target+1; ++i) {
        solSpace[i] = -2; // place holder
    }

    while (arr)



    return 0;
}