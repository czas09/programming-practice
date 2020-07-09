#include <iostream>

int *stack;
int stackTop = 0, size;

void push(int x) {
    if (stackTop == size) {
        std::cout << "\nOverflow";
    } else {
        stack[stackTop++] = x;
    }
}

void pop() {
    if (stackTop == 0) {
        std::cout << "\nUnderflow";
    } else {
        std::cout << "\n" << stack[--stackTop] << " deleted";
    }
}

void show() {
    for (int i = 0; i < stackTop; i++) {
        std::cout << stack[i] << "\n";
    }
}

void topmost() { std::cout << "\nTopmost element: " << stack[stackTop - 1]; }
int main() {
    std::cout << "\nEnter stack_size of stack : ";
    std::cin >> size;
    stack = new int[size];
    int ch, x;
    do {
        std::cout << "\n0. Exit";
        std::cout << "\n1. Push";
        std::cout << "\n2. Pop";
        std::cout << "\n3. Print";
        std::cout << "\n4. Print topmost element:";
        std::cout << "\nEnter Your Choice : ";
        std::cin >> ch;
        if (ch == 1) {
            std::cout << "\nInsert : ";
            std::cin >> x;
            push(x);
        } else if (ch == 2) {
            pop();
        } else if (ch == 3) {
            show();
        } else if (ch == 4) {
            topmost();
        }
    } while (ch != 0);

    delete[] stack;

    return 0;
}