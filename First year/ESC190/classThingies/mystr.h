//  block [a b                  \0]
//  capacity: the size of the block
//  sz: 2

#if !defined(MYSTR_H) // INCLUDE GUARD - so something doesn't blow up if you have more than one header file
typedef struct mystr {
    char *block;
    int sz; // keep track of string length
    int capacity; // keep track of size of the block, 

} mystr;

void create_string(mystr **s); // send address of a pointer

void set_char(mystr *p_s, char c, int ind); // send a pointer to mystr. change p_s->block contents

void append_str(mystr *p_s, const char *src);


#endif