#include <iostream>
using namespace std;

int main() {
    int decimal;
    cout << "Enter a decimal number: ";
    cin >> decimal;

    // Binary conversion
    cout << "Binary: ";
    if (decimal == 0) {
        cout << 0;
    } else {
        int bin[32], i = 0;
        int temp = decimal;
        while (temp > 0) {
            bin[i++] = temp % 2;
            temp /= 2;
        }
        for (int j = i - 1; j >= 0; j--)
            cout << bin[j];
    }
    cout << endl;

    // Octal conversion
    cout << "Octal: ";
    if (decimal == 0) {
        cout << 0;
    } else {
        int oct[32], i = 0;
        int temp = decimal;
        while (temp > 0) {
            oct[i++] = temp % 8;
            temp /= 8;
        }
        for (int j = i - 1; j >= 0; j--)
            cout << oct[j];
    }
    cout << endl;

    // Hexadecimal conversion
    cout << "Hexadecimal: ";
    if (decimal == 0) {
        cout << 0;
    } else {
        char hex[32];
        int i = 0;
        int temp = decimal;
        while (temp > 0) {
            int rem = temp % 16;
            if (rem < 10)
                hex[i++] = rem + '0';
            else
                hex[i++] = rem - 10 + 'A';
            temp /= 16;
        }
        for (int j = i - 1; j >= 0; j--)
            cout << hex[j];
    }
    cout << endl;

    return 0;
}
