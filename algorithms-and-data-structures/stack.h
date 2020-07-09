/**
 * @file stack.h
 * @author czas09
 * @brief Basic operation on a stack as a linked list
 **/

#ifndef STACK_H_
#define STACK_H_

#include <cassert>
#include <iostream>

/**
 * Definition of the node as a linked list
 * \tparam Type type of data nodes of the linked list should contain
 **/
template <class Type>
struct node {
    Type data;           // data at current node
    node<Type> *next;    // pointer to the next ::node instance
};

/**
 * Definition of the stack class
 * \param Type type of data nodes of the linked list in the stack should contain
 **/
template <class Type>
class stack {
  public:
    void display() {
        node<Type> *current = stackTop;
        std::cout << "Top --> ";
        while (current != nullptr) {
            std::cout << current->data << "  ";
            current = current->next;
        }
        std::cout << std::endl;
        std::cout << "Size of stack: " << size << std::endl;
    }

    /** default constructor */
    stack() {
        stackTop = nullptr;
        size = 0;
    }

    /** copy constructor */
    explicit stack(const stack<Type> &otherStack) {
        node<Type> *newNode, *current, *last;

        if (stackTop != nullptr) {
            stackTop = nullptr;
        }
        if (otherStack.stackTop == nullptr) {
            stackTop = nullptr;
        } else {
            current = otherStack.stackTop;
            stackTop = new node<Type>;
            stackTop->data = current->data;
            stackTop->next = nullptr;
            last = stackTop;
            current = current->next;

            while (current != nullptr) {
                newNode = new node<Type>;
                newNode->data = current->data;
                newNode->next = nullptr;
                last->next = newNode;
                last = newNode;
                current = current->next;
            }
        }
        size = otherStack.size;
    }

    /** Destructor */
    ~stack() {}

    /** */
    bool isEmpty() {
        return (stackTop == nullptr);
    }

    /** */
    Type top() {
        assert(stackTop != nullptr);
        return stackTop->data;
    }

    /** */
    void push(Type item) {
        node<Type> *newNode;
        newNode = new node<Type>;
        newNode->data = item;
        newNode->next = stackTop;
        stackTop = newNode;
        size++;
    }

    /** */
    void pop() {
        node<Type> *tmp;
        if (!isEmpty()) {
            tmp = stackTop;
            stackTop = stackTop->next;
            delete tmp;
            size--;
        } else {
            std::cout << "Stack is empty" << std::endl;
        }
    }

    /** */
    void clear() {
        stackTop = nullptr;
    }

    /** overload the "=" operator */
    stack<Type> &operator=(const stack<Type> &otherStack) {
        node<Type> *newNode, *current, *last;

        if (stackTop != nullptr) {
            stackTop = nullptr;
        } else {
            current = otherStack.stackTop;
            stackTop = new node<Type>;
            stackTop->data = current->data;
            stackTop->next = nullptr;
            last = stackTop;
            current = current->next;

            while (current!= nullptr) {
                newNode = new node<type>;
                newNode->data = current->data;
                newNode->next = nullptr;
                last->next = newNode;
                last = newNode;
                current = curret->next;
            }
        }
        size = otherStack.size;
        return *this;
    }

  private:
    node<Type> *stackTop;
    int size;
};

#endif    // STACK_H_