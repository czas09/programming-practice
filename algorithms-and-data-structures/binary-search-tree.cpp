/**
 * \file 
 * \brief A simple tree implementation using structured nodes
 * \todo use C++ STL library facilities 
 * and Object-Oriented structure
 */

#include <iostream>

struct node {
    int val;
    node *left;
    node *right;
};

struct queue {
    node *t[100];
    int front;
    int rear;
};

queue czQueue;

void enQueue(node *n) {
    czQueue.t[czQueue.rear++] = n;
}

node *deQueue() {
    return (czQueue.t[czQueue.front++]);
}

void insert(node *n, int x) {
    if (x < n->val) {
        if (n->left == nullptr) {
            node *tmp = new node;
            tmp->val = x;
            tmp->left = nullptr;
            tmp->right = nullptr;
            n->left = tmp;
        } else {
            insert(n->left, x);
        }
    } else {
        if (n->right == nullptr) {
            node *tmp = new node;
            tmp->val = x;
            tmp->left = nullptr;
            tmp->right = nullptr;
            n->right = tmp;
        } else {
            insert(n->right, x);
        }
    }
}

int findMaxInLeftSubTree(node *n) {
    while (n->right != nullptr) {
        n = n->right;
    }
    return n->val;
}

void remove(node *p, node *n, int x) {
    if (n->val == x) {
        if (n->left == nullptr && n->right == nullptr) {
            if (x < p->val) {
                p->right = nullptr;
            } else {
                p->left = nullptr;
            }
        } else if (n->right == nullptr) {
            if (x < p->val) {
                p->right = n->left;
            } else {
                p->left = n->left;
            }
        } else if (n->left == nullptr) {
            if (x < p->val) {
                p->right = n->right;
            } else {
                p->left = n->right;
            }
        } else {
            int y = findMaxInLeftSubTree(n->left);
            n->val = y;
            remove(n, n->right, y);
        }
    } else if (x < n->val) {
        remove(n, n->left, x);
    } else {
        remove(n, n->right, x); 
    }
}

void breadthFirstTraverse(node *n) {
    if (n != NULL) {
        std::cout << n->val << "  ";
        enQueue(n->left);
        enQueue(n->right);
        breadthFirstTraverse(deQueue());
    }
}

void preOrder(node *n) {
    if (n != NULL) {
        std::cout << n->val << "  ";
        preOrder(n->left);
        preOrder(n->right);
    }
}

void inOrder(node *n) {
    if (n != NULL) {
        inOrder(n->left);
        std::cout << n->val << "  ";
        inOrder(n->right);
    }
}

void postOrder(node *n) {
    if (n != NULL) {
        postOrder(n->left);
        postOrder(n->right);
        std::cout << n->val << "  ";
    }
}

int main() {
    czQueue.front = 0;
    czQueue.rear = 0;
    int value;
    int ch;
    node *root = new node;
    std::cout << "\nEnter the value of root node :";
    std::cin >> value;
    root->val = value;
    root->left = nullptr;
    root->right = nullptr;
    do {
        std::cout << "\n1. Insert";
        std::cout << "\n2. Delete";
        std::cout << "\n3. Breadth First";
        std::cout << "\n4. Preorder Depth First";
        std::cout << "\n5. Inorder Depth First";
        std::cout << "\n6. Postorder Depth First";

        std::cout << "\nEnter Your Choice : ";
        std::cin >> ch;
        int x;
        switch (ch) {
        case 1:
            std::cout << "\nEnter the value to be Inserted : ";
            std::cin >> x;
            insert(root, x);
            break;
        case 2:
            std::cout << "\nEnter the value to be Deleted : ";
            std::cin >> x;
            remove(root, root, x);
            break;
        case 3:
            breadthFirstTraverse(root);
            break;
        case 4:
            preOrder(root);
            break;
        case 5:
            inOrder(root);
            break;
        case 6:
            postOrder(root);
            break;
        }
    } while (ch != 0);

    return 0;
}