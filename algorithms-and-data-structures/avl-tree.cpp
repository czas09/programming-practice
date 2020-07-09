/**
 * \file
 * \brief A simple tree implementation using nodes
 * \todo use C++ STL library facilities and Object-Oriented structure
 */

#include <algorithm>
#include <iostream>
#include <queue>

typedef struct node {
    int data;
    int height;
    struct node *left;
    struct node *right;
} node;

node *createNode(int data) {
    node *n = new node();
    n->data = data;
    n->height = 0;
    n->left = nullptr;
    n->right = nullptr;
    return n;
}

int height(node *root) {
    if (root == nullptr) {
        return 0;
    }
    return 1 + std::max(height(root->left), height(root->right));
}

/** return difference between height of left and right subtree */
int getBalance(node *root) {

}