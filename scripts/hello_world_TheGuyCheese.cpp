#include <iostream>
#include <string>
using namespace std;

class New {
public:
	string ch;

	New() {
		ch = "Hello World!";
}
public:
	void display() {
		cout << ch;
	}

};

int main() {
	New obj1;
	obj1.display();
	return 0;
}