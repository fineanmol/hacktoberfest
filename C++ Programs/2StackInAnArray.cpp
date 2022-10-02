#include <iostream>
#include <stdlib.h>

using namespace std;

class twoStacks
{
    int *arr;
    int size;
    int top1, top2;

public:
    twoStacks(int n)
    {
        size = n;
        arr = new int[n];
        top1 = -1;
        top2 = size;
    }

    void push1(int x)
    {
        if (top1 < top2 - 1)
        {
            top1++;
            arr[top1] = x;
        }
        else
        {
            cout << "Stack Overflow";
            exit(1);
        }
    }

    void push2(int x)
    {

        if (top1 < top2 - 1)
        {
            top2--;
            arr[top2] = x;
        }
        else
        {
            cout << "Stack Overflow";
            exit(1);
        }
    }

    int pop1()
    {
        if (top1 >= 0)
        {
            int x = arr[top1];
            top1--;
            return x;
        }
        else
        {
            cout << "Stack UnderFlow";
            return -1;
        }
    }

    int pop2()
    {
        if (top2 < size)
        {
            int x = arr[top2];
            top2++;
            return x;
        }
        else
        {
            cout <<endl<< "Stack UnderFlow";
            return -1;
        }
    }
    void display()
    {
        cout << "Stack 1 ";
        if (top1 >= 0)
        {
            for (int i = top1; i >= 0; i--)
                cout << arr[i] << " ";
        }
        else
            cout << "Stack is empty";
    
    cout << endl;
    cout << "Stack 2: " ;
    if (top2 != size)
    {
        for (int i = top2; i < size; i++)
        {
            cout << arr[i] << " ";
        }
    }
    else
    {
        cout << "Stack is empty";
    }
    cout << endl;
    }
};

int main()
{
    int n;
    cout << "Enter the size of the stack ";
    cin >> n;

    twoStacks ts(n);
    int ch, val;

    do
    {
        cout << "1) Push in stack 1" << endl;
        cout << "2) Push in stack 2" << endl;
        cout << "3) Pop from stack 1" << endl;
        cout << "4) Pop from stack 2" << endl;
        cout << "5) Display Stack" << endl;
        cout << "6) Exit" << endl;
        cout << "Enter choice: " << endl;
        cin >> ch;
        switch (ch)
        {
        case 1:
        {
            cout << "Enter value to be pushed in stack 1:" << endl;
            cin >> val;
            ts.push1(val);
            break;
        }
        case 2:
        {
            cout << "Enter value to be pushed in stack 2: " << endl;
            cin >> val;
            ts.push2(val);
            break;
        }
        case 3:
        {

            int x = ts.pop1();
            if (x != -1)
            {
                cout << "Popped Value from stack 1 is " << x << endl;
                break;
            }
            break;
        }
        case 4:
        {

            int x = ts.pop2();
            if (x != -1)
            {
                cout << "Popped Value from stack 2 is " << x << endl;
                break;
            }
            break;
        }

        case 5:
        {
            ts.display();
            break;
        }
        case 6:
        {
            cout << "Exit" << endl;
            break;
        }
        default:
        {
            cout << "Invalid Choice" << endl;
        }
        }
        
    } while (ch != 6);
}
