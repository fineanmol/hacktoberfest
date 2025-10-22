#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string str) {
    int n = str.length();
    for (int i = 0; i < n / 2; i++) {
        if (str[i] != str[n - i - 1]) {
            return false; // Not a palindrome
        }
    }
    return true; // It's a palindrome
}

int main() {
    string input;
    cout << "Enter a string or number: ";
    cin >> input;

    if (isPalindrome(input)) {
        cout << input << " is a palindrome." << endl;
    } else {
        cout << input << " is not a palindrome." << endl;
    }

    return 0;
}
