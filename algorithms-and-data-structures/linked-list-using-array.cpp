/**
 * \author czas09
 * 
 * The difference between the linked list using pointer and array: 
 * 1. The NULL is represented by -1;
 * 2. Limited size.
 */

#include <iostream>

struct node {
    int data;
    int next;
};
node AvailArray[100];    // array acts as nodes of a linked list
int head = -1;
int avail = 0;

void initialise_list() {
    for (int i = 0; i <= 98; i++) {
        AvailArray[i].next = i + 1;
    }
    AvailArray[99].next = -1;    // indicating the end of the linked list
}

int getnode() {
    int NodeIndexToBeReturned = avail;
    avail = AvailArray[avail].next;
    return NodeIndexToBeReturned;
}

void freeNode(int nodeToBeDeleted) {
    AvailArray[nodeToBeDeleted].next = avail;
    avail = nodeToBeDeleted;
}

void insertAtBeginning(int data) {
    int newNode = getnode();
    AvailArray[newNode].data = data;
    AvailArray[newNode].next = head;
    head = newNode;
}

void insertAtEnd(int data) {
    int newNode = getnode();
    int tmp = head;
    while (AvailArray[tmp].next != -1) {
        tmp = AvailArray[tmp].next;
    }
}

void display() {
    int tmp = head;
    while (tmp != -1) {
        std::cout << AvailArray[tmp].data << "->";
        tmp = AvailArray[tmp].next;
    }
    std::cout << "-1" << std::endl;
}

int main() {
    initialise_list();
    int x, y, z;
    while(true) {
        std::cout << "1. Insert At The Beginning" << std::endl;
        std::cout << "2. Insert At The End" << std::endl;
        std::cout << "3. Display" << std::endl;
        std::cout << "4.Exit" << std::endl;
        std::cout << "Enter Your choice" << std::endl;
        std::cin >> z;
        switch (z) {
            case 1:
                std::cout << "Enter the number you want to enter" << std::endl;
                std::cin >> x;
                insertAtBeginning(x);
                break;
            case 2:
                std::cout << "Enter the number you want to enter" << std::endl;
                std::cin >> y;
                insertAtEnd(y);
                break;
            case 3:
                std::cout
                    << "The linked list contains the following element in order"
                    << std::endl;
                display();
                break;
            case 4:
                return 0;
            default:
                std::cout << "The entered choice is not correct" << std::endl;
        }
    }

    return 0;
}