#include <iostream>
#include <string>
using namespace std;

class Person {
    string name;
    int age;
public:
    Person(string n, int a) : name(n), age(a) {}
    void birthday() { age++; }
    void display() {
        cout<< name << "! After your bithday you will be " << age << endl;
    }
};

int main() {
    string name;
    int age;
    cout << "Enter name: ";
    cin >> name;
    cout << "Enter age: ";
    cin >> age;

    Person p(name, age);
    p.birthday();
    p.display();
    return 0;
}
