#include "autocomplete.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Function to trim leading spaces
char *trim_leading_spaces(char *str) {
    while (*str == ' ') str++;
    return str;
}

// Compare function for qsort (Alphabetical sorting)
int compare(const void *a, const void *b) {
    return strcmp(((term*)a)->term, ((term*)b)->term);
}

// Compare function for sorting by weight (Descending order)
int comparedouble(const void *a, const void *b) {
    double diff = ((term*)b)->weight - ((term*)a)->weight;
    return (diff > 0) - (diff < 0);
}

// Read in terms from file, sort alphabetically
void read_in_terms(term **terms, int *pnterms, char *filename) {
    FILE *fileptr = fopen(filename, "r");
    if (!fileptr) {
        printf("Error: File not found\n");
        exit(1);
    }

    fscanf(fileptr, "%d\n", pnterms);
    *terms = (term *)malloc(sizeof(term) * (*pnterms));
    if (!*terms) {
        printf("Error: Memory allocation failed\n");
        fclose(fileptr);
        exit(1);
    }

    for (int i = 0; i < *pnterms; ++i) {
        fscanf(fileptr, "%lf %[^\n]", &(*terms)[i].weight, (*terms)[i].term);
        strcpy((*terms)[i].term, trim_leading_spaces((*terms)[i].term)); // Trim leading spaces
    }

    qsort(*terms, *pnterms, sizeof(term), compare); // Sort alphabetically
    fclose(fileptr);
}

// Binary search to find the first occurrence of a matching substring
int lowest_match(term *terms, int nterms, char *substr) {
    int low = 0, high = nterms - 1, result = -1;
    int substr_len = strlen(substr);

    while (low <= high) {
        int mid = (low + high) / 2;
        int cmp = strncmp(terms[mid].term, substr, substr_len);

        if (cmp >= 0) { // Match found or mid term is greater
            if (cmp == 0) result = mid;
            high = mid - 1; // Keep searching left
        } else {
            low = mid + 1;
        }
    }
    return result;
}

// Binary search to find the last occurrence of a matching substring
int highest_match(term *terms, int nterms, char *substr) {
    int low = 0, high = nterms - 1, result = -1;
    int substr_len = strlen(substr);

    while (low <= high) {
        int mid = (low + high) / 2;
        int cmp = strncmp(terms[mid].term, substr, substr_len);

        if (cmp <= 0) { // Match found or mid term is smaller
            if (cmp == 0) result = mid;
            low = mid + 1; // Keep searching right
        } else {
            high = mid - 1;
        }
    }
    return result;
}

// Generate autocomplete results sorted by weight
void autocomplete(term **answer, int *n_answer, term *terms, int nterms, char *substr) {
    int low_index = lowest_match(terms, nterms, substr);
    int high_index = highest_match(terms, nterms, substr);

    if (low_index == -1 || high_index == -1) { // No matches found
        *n_answer = 0;
        *answer = NULL;
        return;
    }

    *n_answer = high_index - low_index + 1;
    *answer = (term *)malloc(sizeof(term) * (*n_answer));
    if (!*answer) {
        printf("Error: Memory allocation failed\n");
        return;
    }

    // Copy matched terms into answer array
    for (int i = 0; i < *n_answer; ++i) {
        strcpy((*answer)[i].term, terms[low_index + i].term);
        (*answer)[i].weight = terms[low_index + i].weight;
    }

    // Sort results by weight (Descending)
    qsort(*answer, *n_answer, sizeof(term), comparedouble);
}

// Main function to test autocomplete
int main(void) {
    term *terms;
    int nterms;
    read_in_terms(&terms, &nterms, "cities2.txt");

    printf("Sorted Terms:\n");
    for (int i = 0; i < nterms; ++i) {
        printf("%lf, %s\n", terms[i].weight, terms[i].term);
    }

    printf("\nTesting lowest and highest match:\n");
    printf("Lowest match index for 'Tor': %d\n", lowest_match(terms, nterms, "Tor"));
    printf("Highest match index for 'Tor': %d\n", highest_match(terms, nterms, "Tor"));

    term *answer;
    int n_answer;
    autocomplete(&answer, &n_answer, terms, nterms, "Tor");

    printf("\nAutocomplete Results for 'Tor':\n");
    for (int i = 0; i < n_answer; ++i) {
        printf("%lf, %s\n", answer[i].weight, answer[i].term);
    }

    // Free allocated memory
    free(terms);
    free(answer);

    return 0;
}
