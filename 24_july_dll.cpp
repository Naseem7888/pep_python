#include <iostream>

struct Node {
    int data;
    Node* next;
    Node* prev;
};

void insertAtHead(Node*& head, int newData) {
    Node* newNode = new Node();
    newNode->data = newData;
    newNode->next = head;
    newNode->prev = nullptr;
    if (head != nullptr) {
        head->prev = newNode;
    }
    head = newNode;
}

void insertAtTail(Node*& head, int newData) {
    Node* newNode = new Node();
    newNode->data = newData;
    newNode->next = nullptr;
    if (head == nullptr) {
        newNode->prev = nullptr;
        head = newNode;
        return;
    }
    Node* last = head;
    while (last->next != nullptr) {
        last = last->next;
    }
    last->next = newNode;
    newNode->prev = last;
}

void deleteNode(Node*& head, int key) {
    Node* current = head;
    while (current != nullptr && current->data != key) {
        current = current->next;
    }
    if (current == nullptr) {
        return;
    }
    if (current->prev != nullptr) {
        current->prev->next = current->next;
    } else {
        head = current->next;
    }
    if (current->next != nullptr) {
        current->next->prev = current->prev;
    }
    delete current;
}

void printListForward(Node* node) {
    while (node != nullptr) {
        std::cout << node->data << " ";
        node = node->next;
    }
    std::cout << std::endl;
}

void printListBackward(Node* node) {
    if (node == nullptr) {
        return;
    }
    while (node->next != nullptr) {
        node = node->next;
    }
    while (node != nullptr) {
        std::cout << node->data << " ";
        node = node->prev;
    }
    std::cout << std::endl;
}

int main() {
    Node* head = nullptr;

    insertAtHead(head, 5);
    insertAtTail(head, 10);
    insertAtHead(head, 2);
    insertAtTail(head, 15);

    printListForward(head);
    printListBackward(head);

    deleteNode(head, 10);
    printListForward(head);

    deleteNode(head, 2);
    printListForward(head);

    return 0;
}