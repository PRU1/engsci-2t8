#include "autocomplete.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int compare(const void *a, const void *b){
    const term *aa = a;
    const term *bb = b;
   return strcmp(aa->term, bb->term);

}
int comparedouble(const void *a, const void *b) {
    double diff = ((term*)b)->weight - ((term*)a)->weight;
    return (diff > 0) - (diff < 0);
}
char *cutspaces(char *str) {
    while (*str == ' ') str++;
    return str;
}
void read_in_terms(term **terms, int *pnterms, char *filename) {
    FILE *fileptr = fopen(filename, "r");
    if (!fileptr) {
        printf("File not found\n");
        exit(1);
    }

    fscanf(fileptr, "%d\n", pnterms);
    *terms = (term *)malloc(sizeof(term) * (*pnterms));
    if (!*terms) {
        printf("Memory allocation failed\n");
        exit(1);
    }

    for (int i = 0; i < *pnterms; ++i) {
        //fscanf(fileptr, "%lf %[^\n]", &(*terms)[i].weight, (*terms)[i].term);
        fscanf(fileptr, "%lf %[^\n]", &(*terms)[i].weight, (*terms)[i].term);
        strcpy((*terms)[i].term, cutspaces((*terms)[i].term));  // Trim spaces

    }

    qsort(*terms, *pnterms, sizeof(term), compare); // alpha order terms
    fclose(fileptr);
}
/*
void read_in_terms2(term **terms, int *pnterms, char *filename) {
    FILE *fileptr = fopen(filename, "r");
    if (!fileptr) {
        printf("File not found");
        exit(1);
    }
    fscanf(fileptr, "%d\n", pnterms);
    // memory block terms
    *terms = (term *)malloc(sizeof(term)*(*pnterms));
    for (int i = 0; i < *pnterms; ++i) {
        fscanf(fileptr, "\n%lf %[^\n]", &(*terms)[i].weight, (*terms)[i].term);
    }
    // alpha order the terms
    qsort(*terms, *pnterms, sizeof(term), compare);
    fclose(fileptr);
}
*/

int lowest_match(term *terms, int nterms, char *substr) {
    // binary search of first match
    // binary search pseudocode --> low, high, mid. eliminate half by half until you get a match, or low==high 
    int low = 0; int high = nterms-1; int result = -1;
    int substrSz = strlen(substr);
    while (low <= high){
        int mid = (low+high)/2; 
        int comparison = strncmp(terms[mid].term, substr, substrSz);

        if(comparison >= 0) { // scrap above mid
            // equality
            if (comparison == 0) {
                result = mid;
            }
            high = mid-1;
        }
        else{
            low = mid+1;
        }
    }
    return result; // return -1 if no int found 
}
int highest_match(struct term *terms, int nterms, char *substr) {
    // binary search of first match
    // binary search pseudocode --> low, high, mid. eliminate half by half until you get a match, or low==high 
    int low = 0; int high = nterms-1; int result = -1;
    int substrSz = strlen(substr);
    while (low <= high){
        int mid = (low+high)/2; 
        int comparison = strncmp(terms[mid].term, substr, substrSz);

        if(comparison <= 0) { // scrap above mid
            // equality
            if (comparison == 0) {
                result = mid;
            }
            low = mid+1; // search right
        }
        else{
            high = mid-1;
        }
    }
    return result; // return -1 if no int found 

 }
void autocomplete(term **answer, int *n_answer, term *terms, int nterms, char *substr) {
    // dump answers between low and high indices into *answer
    int low_index = lowest_match(terms, nterms, substr);
    int high_index = highest_match(terms, nterms, substr);
    *n_answer = high_index-low_index + 1;
    *answer = (term *)malloc(sizeof(term)*(*n_answer));

    if (low_index == -1 || high_index == -1) {
        printf("No answer found");
        return;
    }

    // dump answers into answers
    for (int i = 0; i < *n_answer; ++i) {
        strcpy((*answer)[i].term, terms[i+low_index].term);
        (*answer)[i].weight = terms[low_index+i].weight;
    }
    // sort by weight
    qsort(*answer, *n_answer, sizeof(term), comparedouble);
}


int main(void)
{
    struct term *terms;
    int nterms;
    read_in_terms(&terms, &nterms, "cities.txt");
    for (int i = 0; i < nterms; ++i) {
        printf("%lf, %s \n", terms[i].weight, terms[i].term);
        // what
    }
    printf("%d", lowest_match(terms, nterms, "Tok"));
    printf("%d", highest_match(terms, nterms, "Tor"));
    //highest_match(terms, nterms, "Tor");
    
    struct term *answer;
    int n_answer;
    autocomplete(&answer, &n_answer, terms, nterms, "Tor");
    printf("\n\n\n");
    for (int i = 0; i < n_answer; ++i) {
        printf("%lf, %s \n", answer[i].weight, answer[i].term);
        // what
    }

    //free allocated blocks here -- not required for the project, but good practice
    return 0;
}

