#include <iostream>
#include <list>

struct node {
    int val;
    node *left;
    node *right;
};

void createBT(node *current, node *n, int x, char pos) {
    if (n != nullptr) {
        char ch;
        std::cout << "\nLeft or right of " << n->val << ": ";
        std::cin >> ch;
        if (ch == 'l') {
            createBT(n, n->left, x, ch);
        } else if (ch == 'r') {
            createBT(n, n->right, x, ch);
        }
    } else {
        node *t = new node;
        t->val = x;
        t->left = nullptr;
        t->right = nullptr;
        if (pos == 'l') {
            current->left = t;
        } else if (pos = 'r') {
            current->left = t;
        }
    }
}

void breadthFirstTraverse(node *n) {
    std::list<node *> queue;
    queue.push_back(n);

    while (!queue.empty()) {
        n = queue.front();
        std::cout << n->val << "  ";
        queue.pop_front();

        if (n->left != nullptr) {
            queue.push_back(n->left);
        }
        if (n->right != nullptr) {
            queue.push_back(n->right);
        }
    }
}

void preOrder(node *n) {
    if (n != nullptr) {
        std::cout << n-> val << "  ";
        preOrder(n->left);
        preOrder(n->right);
    }
}

void inOrder(node *n) {
    if (n != nullptr) {
        inOrder(n->left);
        std::cout << n->val << "  ";
        inOrder(n->right);
    }
}

void postOrder(node *n) {
    if (n != nullptr) {
        postOrder(n->left);
        postOrder(n->right);
        std::cout << n->val << "  ";
    }
}

int main() {
    int value;
    int ch;
    node *root = new node;
    std::cout << "\nEnter the value of root node: ";
    std::cin << value;
    root->val = value;
    root->left = nullptr;
    root->right = nullptr;

    do {
        std::cout << "\n1. Insert";
        std::cout << "\n2. Breadth First Traverse";
        std::cout << "\n3. Preorder Traverse (Depth First)";
        std::cout << "\n4. Inorder Traverse (Depth First)";
        std::cout << "\n5. Postorder Traverse (Depth First)";
        std::cout << "\nEnter Your Choice: ";
        std::cin >> ch;

        switch (ch) {
            case 1:
                int x;
                char pos;
                std::cout << "\nEnter the value to be inserted: ";
                std::cin >> x;
                std::cout << "\nLeft of Right of root: ";
                std::cin >> pos;
                if (pos = 'l') {
                    createBT(root, root->left, x, pos);
                } else if (pos = 'r') {
                    createBT(root, root->right, x, pos);
                }
                break;
            case 2: 
                breadthFirstTraverse(root);
                break;
            case 3: 
                preOrder(root);
                break;
            case 4: 
                inOrder(root);
                break;
            case 5: 
                postOrder(root);
                break;
        }
    } while (ch != 0);
}