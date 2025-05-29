#include<stdio.h>

int linear_search(int*a, int sz, int elem){
    for (int i = 0; i < sz; ++i){
        if (*(a+i) == elem ) {
            return i;
        }
    }
    return 0;
}

void reverse_arr(int *arr, int sz){
    for (int i = 0; i < sz/2; ++i){
        int temp = *(arr+i);
        arr[i] = arr[sz-1-i];
        arr[sz-1-i] = temp;


    }
}
int main () {
    
    int a[] = {1,2,3,4,4,5};
    printf("%d", linear_search(a, 6, 4));
    reverse_arr(a, 6);
    printf("\n");
    for (int i = 0; i < 6; ++i) {
        printf("%d ", a[i]);
    }


    return 0;
}