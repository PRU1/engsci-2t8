#include <stdio.h>
int odd_element_sum(int *arr, int size) {
    int sum = 0; 
    for (int i = 0; i < size; ++i) {
        if (arr[i] % 2 != 0) {
            sum += arr[i];
        }
    }
    return sum;
}
void string_parse(char *charArr) {
    while (*charArr) { // iterate until the null character
        printf("%c ", *charArr);
        charArr++;
    }
}
int main () {
    int arr[] = {1,2,3,4,5,6,7,8,9};
    char yay[] = "abcdeggihs";
    int size = sizeof(arr)/sizeof(arr[0]);
    printf("%d", odd_element_sum(arr, 9));
    //string_parse(yay);

    return 0;
}