#if !defined(LL_H)
#define LL_H

 typedef struct node{
    int data;
    struct node *next;
 } node;

 typedef struct LL{
    node *head;
    int size;
 } LL;


void create_node(node **n, int data);

void LL_append(LL *my_list, int new_elem);

int validate_list(LL *my_list);

void print_linkedList(LL *my_list);

int get_i(LL *my_list, int index);

#endif