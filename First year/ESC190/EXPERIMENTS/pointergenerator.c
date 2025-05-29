#include<stdio.h>

int main () {
    const int num = 1000;
    for (int i = 0; i < num; ++i) {
        printf("*");
    }

    printf("\n\n\n");

    for (int i = 0; i < num; ++i){
        printf("&");
    }


    return 0;
}