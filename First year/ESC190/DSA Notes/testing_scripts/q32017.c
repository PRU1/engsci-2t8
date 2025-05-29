#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
} Node;

void init(Node *tree) {
    tree->data = 0;
    tree->left = NULL;
    tree->right = NULL;
}

int sumBST(Node *tree) {
    // traverse through binary tree
    // base case: at null. return 0
    if (tree == NULL) {
        return 0;
    }
    else {
        int s1 = 0;
        if (tree->data > 10) {
            s1 = tree->data;
        }
        return s1 + sumBST(tree->left) + sumBST(tree->right);
    }
}

#define NODES 6
typedef struct adjMat {
    int matrix[NODES][NODES];
    int vNodes[NODES];
} adjMat;

struct Data {
    int value;
};

struct Stack * initStack() ;




int main () {

    Node *n1 = malloc(sizeof(Node));
    n1->data = 19;
    Node *n2 = malloc(sizeof(Node));
    n2->data = 5;
    Node *n3 = malloc(sizeof(Node));
    n3->data = 20;
    Node *n4 = malloc(sizeof(Node));
    n4->data = 2;
    Node *n5 = malloc(sizeof(Node));
    n5->data = 18;

    n1->left = n2; n1->right = n3;
    n2->left = n4; n2->right = n5;
    n3->right=NULL; n3->left=NULL; n4->right=NULL; n4->left=NULL; n5->right=NULL; n5->left=NULL;

    printf("%d", sumBST(n1));
    



}