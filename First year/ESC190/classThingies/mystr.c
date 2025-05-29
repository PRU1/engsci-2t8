#include "mystr.h"
#include <stdlib.h>

void create_string(mystr **p_p_s) {
    *p_p_s = (mystr *)malloc(sizeof(mystr)); 
    // error checking
    if (*p_p_s == NULL) {
        printf("error failed to create empty string naurrrrrr");
        exit(1);
    }
    // set some starting capacity
    (*p_p_s)->capacity = 100;
    (*p_p_s)->block = (char *)malloc(((*p_p_s)->capacity)*sizeof(char));
    if ((*p_p_s)->block == NULL) {
        printf("error failed to create block");
        exit(1);
    }
     // NOTE NULL is not the same as '\0'. '\0' means a terminating character in a string

    // function input is (create_string(&p_s))
}


void set_char(mystr *p_s, int ind, char c) {
    (p_s->block)[ind] = c;
    if ((ind >= p_s->sz) || ind < 0)  {
        printf("ERROR: index %d out of range", p_s->sz);
        exit(1);
    }
}

void append_str(mystr *p_s, const char *src) {
    // can't use strcat because you might not have enough capacity
    if (p_s->capacity < p_s->sz + strlen(src)) // if not enough capacity, boost your capacity 
        {
            int new_capacity = (p_s->capacity + strlen(src)+1)*2; // just make it biggerr to avoid allocating again
            p_s->block = (char *)realloc(p_s->block, new_capacity*sizeof(char)); // reallocate the block with new_capacity 
            p_s->capacity = new_capacity;
            p_s->sz = strlen(src) + p_s->capacity; // new size is new string length + old size
    }
    strcat(p_s->block, src); 
}