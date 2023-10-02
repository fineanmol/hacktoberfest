// LANGUAGE: C++
// AUTHOR: Suryansh Singh
// GITHUB: https://github.com/suryanshsingh2001

// Blinking hello world
#include <iostream>
#include <chrono>
#include <thread>

using namespace std;

void clearScreen()
{

    system("cls");
}

int main()
{
    while (true)
    {
        cout << "Hello, World!" << endl;
        this_thread::sleep_for(chrono::seconds(1));
        clearScreen();
        this_thread::sleep_for(chrono::seconds(1));
    }
    return 0;
}
