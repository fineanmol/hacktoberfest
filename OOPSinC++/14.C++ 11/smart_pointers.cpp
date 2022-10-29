//JAVA, C#,.net langs provide mechanism to collect the garbage memory from
//heap after program is executed

//Smart Pointers provide a mechanism to deallocate memory from heap after program is terminated
//3 smart pointers available in c++:
//1.unique_ptr
//2.shared_ptr
//3.weak_ptr
#include <iostream>
using namespace std;


int Fib(struct Rectangle *r1){
    r1->length++;
    return r1->length * r1->breadth;
    
}
struct Rectangle{
    int length;
    int breadth;
};
int main() {
    struct Rectangle r={10,5};
	cout<<Fib(&r);
	
	return 0;
}

Intro
input and output streams
java.io classes
file input stream file reader
byte streams -char array reader
buffered streams-buffered reader
piped streamsize
random access file
file class
serialization
print stream
data streams
object streams

