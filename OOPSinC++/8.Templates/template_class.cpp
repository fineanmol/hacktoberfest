#include<iostream>
using namespace std;

template <class T>
class Stack{
    private:
    T S[10];
    int top;

    public:
    void push(T x);
    T pop();
};
template<class T>
void Stack<T>::push(T x){

}

template<class T>
T Stack<T>::pop(){

}

int main()
{
    Stack<int> S;
    Stack<float> S2;
    return 0;
}