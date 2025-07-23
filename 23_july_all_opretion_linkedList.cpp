#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int value) : data(value), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;

public:
    LinkedList() : head(nullptr) {}

    ~LinkedList() {
        while (head != nullptr) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }

    void insertAtBeginning(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }

    void insertAtEnd(int value) {
        Node* newNode = new Node(value);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    void deleteNode(int value) {
        if (head == nullptr) {
            return;
        }

        if (head->data == value) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
           
        Node* current = head;
        while (current->next != nullptr && current->next->data != value) {
            current = current->next;
        }

        
        if (current->next != nullptr) {
            Node* temp = current->next;
            current->next = temp->next;
            delete temp;
        }
    }

    void display() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << "->";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }
};

int main() {
    LinkedList list;

    list.insertAtBeginning(10);
    list.insertAtBeginning(40);
    list.insertAtEnd(99);
    list.insertAtBeginning(70);

    cout << "Original list:" << endl;
    list.display();

    cout << "\nDeleting node with value 40:" << endl;
    list.deleteNode(40);
    list.display();

    cout << "\nDeleting node with value 70 (head):" << endl;
    list.deleteNode(70);
    list.display();

    cout << "\nDeleting node with value 99 (tail):" << endl;
    list.deleteNode(99);
    list.display();

    cout << "\nAttempting to delete non-existent node with value 50:" << endl;
    list.deleteNode(50);
    list.display();

    return 0;
}