/*
 * Project: LRU Cache Implementation
 * Language: C++
 * Author: [Your Name]
 * Hacktoberfest Contribution 2025
 *
 * Description:
 * This program implements a Least Recently Used (LRU) Cache using a combination of
 * a Doubly Linked List and an Unordered Map (Hash Map) to achieve O(1) time
 * complexity for both get() and put() operations.
 *
 * The cache stores key-value pairs and automatically removes the least recently used
 * item when the cache reaches its capacity.
 *
 * Operations:
 *  - get(key): Returns the value of the key if present, otherwise -1.
 *  - put(key, value): Inserts or updates the key-value pair.
 *
 * Algorithmic Complexity:
 *  - Time:  O(1)
 *  - Space: O(n)
 */
#import <unordered_map>
using namespace std;

//Node class for creating elements of doubly linked list
class Node{
    public:
    int key;
    int value;
    Node*prev;
    Node*next;


Node(int key, int value){
    this->key=key;
    this->value=value;
    prev=NULL;
    next=NULL;
}
};
//Class which manages cache behaviour

class LRUCache {
public:
   unordered_map<int, Node*>mpp;
   int capacity;
   Node*head; // Dummy Head (Most recently used)

   Node*tail;
   

  
    LRUCache(int capacity) {
        this->capacity=capacity;
        mpp.clear();
        head= new Node(0,0);
        tail= new Node(0,0);

        head->next=tail;
        tail->prev=head;
    }
  void deleteNode(Node*node){
    Node*prevNode= node->prev;
   Node*afterNode=node->next;

    prevNode->next= afterNode;
    afterNode->prev= prevNode;
  }

  void InsertAfterHead(Node*node){
    Node*currentAfterHead=head->next;
    head->next=node;
    node->prev=head;
    node->next= currentAfterHead;
    currentAfterHead->prev=node;

  }
    
    int get(int key) {
        if(mpp.find(key)==mpp.end())
         return -1;

        Node*node= mpp[key];
        deleteNode(node);
        InsertAfterHead(node);

        return node->value;
    }
    
    void put(int key, int value) {
       if(mpp.find(key)!=mpp.end()){

        Node*node=mpp[key];
        node->value=value;
        deleteNode(node);
        InsertAfterHead(node);
        return;
       }
     if(mpp.size()==capacity){
        Node*node=tail->prev;
        mpp.erase(node->key);
        deleteNode(node);
        delete node;

     }
     Node*node= new Node(key, value);
     mpp[key]=node;
     InsertAfterHead(node);
    }

};
