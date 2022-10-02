#include <bits/stdc++.h>
using namespace std;

template <typename T>
class Node
{
public:
    string key;
    T value;
    Node<T> *next;

    Node(string key, T val)
    {
        this->key = key;
        value = val;
        next = nullptr;
    }
    ~Node()
    {
        if (next != nullptr)
        {
            // this delete the all the next nodes and this node
            delete next;
        }
    }
};

template <typename T>
class HashTable
{
    Node<T> **table; // pointer to an array of functions
    int curr_size;
    int table_size;

    int hashFunc(string key)
    {
        int idx = 0;
        // power
        int p = 1;
        for (int j = 0; j < key.length(); j++)
        {
            idx = idx + (key[j] * p) % table_size;
            idx = idx % table_size;
            // we are multiplying with the 27 that is prime
            p = (p * 27) % table_size;
        }
        return idx;
    }

    void rehash()
    {
        Node<T> **oldTable = table;
        int oldTableSize = table_size;
        table_size = 2 * table_size;
        table = new Node<T> *[table_size];

        // initialize the new table with the null ptr
        for (int i = 0; i < table_size; i++)
        {
            table[i] = nullptr;
        }

        // shift the nodes in to the new table
        for (int i = 0; i < oldTableSize; i++)
        {
            Node<T> *temp = oldTable[i];
            while (temp != nullptr)
            {
                insert(temp->key, temp->value);
                temp = temp->next;
            }

            if (oldTable[i] != nullptr)
            {
                delete oldTable[i];
            }
        }

        // and at the last delete the whole table
        delete[] oldTable;
    }

public:
    HashTable(int ts = 7)
    {
        table_size = ts;
        table = new Node<T> *[table_size];
        curr_size = 0;
        // initialling the array here
        for (int i = 0; i < table_size; i++)
        {
            table[i] = nullptr;
        }
    }

    void insert(string key, int val)
    {

        int idx = hashFunc(key);

        Node<T> *n = new Node<T>(key, val);
        // for the first time table[idx] is null and we are inserting at the front
        n->next = table[idx];
        table[idx] = n;
        curr_size++;

        // load factor
        float loadFactor = curr_size / (1.0 * table_size);

        // rehash...
        // if (loadFactor > 0.75)
        // {
        //     rehash();
        // }
    }

    void print()
    {
        for (int i = 0; i < table_size; i++)
        {
            cout << "Bucket " << i << "-> ";
            Node<T> *temp = table[i];
            while (temp != nullptr)
            {
                cout << temp->value << "-";
                temp = temp->next;
            }
            cout << endl;
        }
    }

    T *search(string key)
    {
        int idx = hashFunc(key);
        Node<T> *llist = table[idx];
        while (llist != nullptr)
        {
            if (llist->key == key)
            {
                return &llist->value;
            }
            llist = llist->next;
        }

        return nullptr;
    }

    void erase(string key)
    {
        int idx = hashFunc(key);
        Node<T> *llist = table[idx];
        Node<T> *prev=llist;
        if(prev->key==key){
            Node<T> *temp=llist->next;
            llist->next=nullptr;
            table[idx]=temp;
            delete llist;
            return;
        }
        while (llist!=nullptr)
        {
            if (llist->key == key)
            {
                Node<T> *temp=llist->next;
                llist->next=nullptr;
                prev->next=temp;
                delete llist;
                cout<<"erased"<<endl;
                break;
            }
            prev=llist;
            llist = llist->next;
        }
    }
};

int main()
{
    HashTable<int> mp(10);

    mp.insert("rohit", 1);
    mp.insert("rahul", 2);
    mp.insert("sakshi", 3);
    mp.insert("amfdsit", 4);
    mp.insert("rodsfshit", 5);
    mp.insert("rafdshul", 6);
    mp.insert("sakshssi", 7);
    mp.insert("amiwt", 8);
    mp.insert("roahit", 9);
    mp.insert("rashul", 10);
    mp.insert("sakfshi", 11);
    mp.insert("amict", 12);
    mp.print();

    int *t = mp.search("dsfsadf");
    if (t)
    {
        cout <<*t<<endl;
    }else{
        cout<<"Not found"<<endl;
    }
    mp.erase("amfdsit");
    mp.print();


    return 0;
}