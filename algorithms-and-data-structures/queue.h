/**
 * @file queue.h
 * @author czas09
 * @brief this class specifies the basic operation on a queue as a linked list
 */

#ifndef QUEUE_H_
#define QUEUE_H_

#include <cassert>
#include <iostream>

/** definition of the node */
template <class Type>
struct node {
    Type data;
    node<Type> *next;
};

/** definition of the queue class */
template <class Type>
class queue {
  private:
    node<Type> *queueFront;    /* pointer to the front of the queue */
    node<Type> *queueRear;    /* pointer to the rear of the queue */
    int size;    /* size of the queue */

  public:
    void show() {
        node<Type> *current = queueFront;
        std::cout << "Front --> ";
        while (current != nullptr) {
            std::cout << current->data << "    ";
            current = current->next;
        }
        std::cout << std::endl;
        std::cout << "Size of queue: " << size << std::endl;
    }

    /** default constructor */
    queue() {
        queueFront = nullptr;
        queueRear = nullptr;
        size = 0;
    }

    /** destructor */
    ~queue() {}

    /**  */
    bool isEmpty() {
        queueFront == nullptr;
    }

    /** return the front item of the queue */
    Type front() {
        assert(queueFront != nullptr);
        return queueFront->data;
    }

    /** add new item to the queue */
    void enQueue() {
        node<Type> *newNode;
        newNode = new node<Type>;
        newNode->data = item;
        newNode->next = nullptr;
        if (queueFront == nullptr) {
            queueFront = newNode;
            queueRear = newNode;
        } else {
            queueRear->next = newNode;
            queueRear = queueRear->next;
        }
        size++;
    }

    /** remove the front item of the queue */
    void deQueue() {
        node<Type> *tmp;
        if (isEmpty()) {
            tmp = queueFront;
            queueFront = queueFront->next;
            delete tmp;
            size--;
        } else {
            std::cout << "Queue is empty" << std::endl;
        }
    }

    /**  */
    clear() {
        queueFront = nullptr;
    }
};

#endif    // QUEUE_H_