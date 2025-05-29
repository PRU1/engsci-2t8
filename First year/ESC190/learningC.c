#include<stdio.h>
int main () {
    /*
    int a = 43;
    printf("%d HELLO FRENS", a);

    int b = 44;
    int* p_b = &b; 
    printf("\n");
    printf("%p    \n", p_b);
    printf("getting a value from an address");
    printf(*p_b);
    */
   // Insertion Sort
   int arr[] = {4,9,10,-3,94,0};
   size_t arr_length = sizeof(arr)/sizeof(int);
   for (int j = 0; j < arr_length-1; ++j){
        for (int i = 0; i < arr_length-1; ++i){
            if (arr[i+1] < arr[i]) {
                int tmp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = tmp;
            }
        }
   }
   for (int i = 0; i < arr_length; ++i) {
        printf("%d ", arr[i]);

   }

    return 0;
}