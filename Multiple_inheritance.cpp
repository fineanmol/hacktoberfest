#include <bits/stdc++.h>
using namespace std;

class A{
    public:
    int a=1;
    int b=2;
};
class B{
    public:
    int c=3;
};
class C:public A,public B{
    public:
    int d=4;
};
int main() {
	// your code goes here
    C obj;
    cout<<obj.a<<" "<<obj.c;

    
	return 0;
}
