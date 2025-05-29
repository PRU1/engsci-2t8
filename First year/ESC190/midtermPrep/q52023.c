#include <stdio.h>
#include <stdlib.h>

typedef struct business {
    int phone_number[10];  // Array to store phone number digits
    char *name;            // Dynamically allocated business name
} business;

void read_numbers(const char *filename, business **whitepages, int *size) {
    // open file
    FILE *ptr = fopen(filename, "r");
    if (ptr == NULL) {
        printf("error, can't find file");
    }
    // read number
    fscanf(ptr, "%d\n", size);
    (*whitepages) = malloc(*size *sizeof(business));
    for (int i = 0; i < *size; ++i) {
        char phone_number[15];
        fscanf(ptr, "%s", phone_number);
        // parse phone number 
        int k = 0;
        for (int j = 0; phone_number[j] != '\0'; ++j) {
            if (phone_number[j] == '-');
            else {
                (*whitepages)[i].phone_number[k] = phone_number[j];
                ++k;
            }
        }
        // read the remaining stuff after the tab character
        fgetc(ptr); // consume tab after phone number
        int capacity = 10;
        int length = 0;
        char *name = malloc(sizeof(char)*capacity);
        char curChar;
        while ((curChar = fgetc(ptr)) != '\n' && curChar != EOF) {
            if (length+1 >= capacity) {
                // resize
                char *temp = realloc(name, capacity+10);
                capacity += 10;
                name = temp;
            }
            name[length++] = curChar;
        }
        name[length] = '\0'; // get this here yayyy
        // push your changes to white_pages
        // strcpy((*whitepages)[i].name, name);
        (*whitepages)[i].name = name;

    }
    fclose(ptr);
    // parse business name
}

void free_whitepages(business *whitepages, int size) {
    for (int i = 0; i < size; i++) {
        free(whitepages[i].name);  // Free each business name
    }
    free(whitepages);  // Free struct array
}

int main() {
    business *whitepages = NULL;
    int size = 0;

    read_numbers("file.txt", &whitepages, &size);

    // Print results
    for (int i = 0; i < size; i++) {
        printf("Phone: ");
        for (int j = 0; j < 10; j++) {
            printf("%d", whitepages[i].phone_number[j]);
            if (j == 2 || j == 5) printf("-");  // Format phone number
        }
        printf(", Business: %s\n", whitepages[i].name);
    }

    // Free allocated memory
    free_whitepages(whitepages, size);
    return 0;
}
