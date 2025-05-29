#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void count_letters(char *s, int counts[]) {
    while (*s) {
        // convert char to int: - '0'
        if (*s >= 'a' && *s <= 'z') {
            counts[(int) *s - 'a']++;
        }
        ++s;
    }

}

char* reverse_words(char *str) {
    // traverse the string backwards
    // have a tempory string, fill it up
    // add it to output string in reverse order

    int len = strlen(str);
    char *output = malloc(sizeof(char)*(len+1));
    int wordSize = 0;
    int outputIndex = 0;

    char *temp = malloc(sizeof(char)*(len+1)); // make sure to keep track of end... probably don't need to
    for (int i = len-1; i >= 0; --i) {
        if (str[i] != ' ') {
            temp[wordSize++] = str[i];
        }
        else {
            // oh no we hit a space! dump everything in temp into output
            for (int j = wordSize-1; j >= 0; --j) {
                output[outputIndex++] = temp[j];
            }
            wordSize = 0; 
            output[outputIndex++] = ' ';
        }

    }
    output[len] = '\0';
    return output;
}

int is_increasing(int *arr, int sz) {
    // if the first element doesn't equal the second element and the second element onwards is increasing 
    if (sz-1 == 0) {
        return 1;
    }
    else if (is_increasing(arr+1, sz-1) == 1 && *arr != *(arr+1)) {
        return 1;
    } 
    else {
        return 0;
    }

}

int main () {

    char *s = " hola amegos hellothere testing";
    int arrr[] = {1,2,2,4,5};
    printf("%d", is_increasing(arrr, 5));

/*
    char *tmp = reverse_words(s);
    
     while (*tmp) {
         printf("%c", *tmp);
         ++tmp;
     }
*/

    return 0;
}