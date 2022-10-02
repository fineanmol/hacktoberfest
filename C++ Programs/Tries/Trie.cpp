#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    char data;
    bool isTerminal;
    unordered_map<char, Node*> m;

    Node(char d)
    {
        data = d;
        isTerminal = false;
    }
};

class Trie
{
    Node*root;
public:
    Trie(){
        root=new Node('\0'); 
    }

    void insert(string word){
        //assigning the temp  variable as the root
        Node* temp=root;

        for(auto ch:word){
            
            //we assign only one time we insert the word so that we dont need to assign the
            //the indexes again and again 
            if(temp->m.count(ch)==0){
                Node *n=new Node(ch);
                //assingnin the new node and also made the mapping according to
                //the character
                temp->m[ch]=n;
            }

            //shifting the temp pointer to the newly created node
            temp=temp->m[ch];
        }
        //making the end node as the terminal node
        temp->isTerminal=true;
    }

    bool search(string word){
        Node* temp=root;

        for(auto ch:word){

            if(temp->m.count(ch)==0){
                return false;
            }
            temp=temp->m[ch];
        }
        
        //the temp has now reached the end of the word then 
        //check if it terminal
        return temp->isTerminal;
    }

};

class SuffixTrie
{
    Node*root;

    void insert_helper(string word){
        //assigning the temp  variable as the root
        Node* temp=root;

        for(auto ch:word){
            
            //we assign only one time we insert the word so that we dont need to assign the
            //the indexes again and again 
            if(temp->m.count(ch)==0){
                Node *n=new Node(ch);
                //assingnin the new node and also made the mapping according to
                //the character
                temp->m[ch]=n;
            }

            //shifting the temp pointer to the newly created node
            temp=temp->m[ch];
        }
        //making the end node as the terminal node
        temp->isTerminal=true;
    }
public:
    SuffixTrie(){
        root=new Node('\0'); 
    }

    

    bool search(string word){
        Node* temp=root;

        for(auto ch:word){

            if(temp->m.count(ch)==0){
                return false;
            }
            temp=temp->m[ch];
        }
        
        //the temp has now reached the end of the word then 
        //check if it terminal
        return temp->isTerminal;
    }

    void insert(string word){
        for(int i=0;i<word.length();i++){
            insert_helper(word.substr(i));
        }
    }

};

int main()
{

    // vector<string> words{"apple","app","apron","apricot","mango", "mangobite "};
    
    // Trie *trie1=new Trie();

    // for(auto word:words){
    //     trie1->insert(word);
    // }

    // (trie1->search("apple"))?cout<<"apple":cout<<"wrong"<<endl;

    SuffixTrie st=SuffixTrie();

    st.insert("hello");

    vector<string> wrds{"hello","ello","llo","lo","o"};
    for(auto wrd:wrds){
        cout<<st.search(wrd)<<endl;
    }

    return 0;
}