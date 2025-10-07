#include <iostream>
using namespace std;

// Decimal to Binary
void decimal_binary(int decimal) {
    cout << "Binary: ";
    if (decimal == 0) {
        cout << 0 << endl;
        return;
    }
    int bin[32], i = 0;
    int temp = decimal;
    while (temp > 0) {
        bin[i++] = temp % 2;
        temp /= 2;
    }
    for (int j = i - 1; j >= 0; j--)
        cout << bin[j];
    cout << endl;
}

// Decimal to Octal
void decimal_octal(int decimal) {
    cout << "Octal: ";
    if (decimal == 0) {
        cout << 0 << endl;
        return;
    }
    int oct[32], i = 0;
    int temp = decimal;
    while (temp > 0) {
        oct[i++] = temp % 8;
        temp /= 8;
    }
    for (int j = i - 1; j >= 0; j--)
        cout << oct[j];
    cout << endl;
}

// Decimal to Hexadecimal
void decimal_hex(int decimal) {
    cout << "Hexadecimal: ";
    if (decimal == 0) {
        cout << 0 << endl;
        return;
    }
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
    cout << endl;
}

// Binary to Decimal
int binary_decimal(long binary) {
    int decimal = 0, base = 1;
    long temp = binary;
    while (temp > 0) {
        int digit = temp % 10;
        if (digit != 0 && digit != 1) {
            cout << "Invalid binary number!" << endl;
            return -1;
        }
        temp /= 10;
    }
    while (binary > 0) {
        int last = binary % 10;
        decimal += last * base;
        base *= 2;
        binary /= 10;
    }
    return decimal;
}

// Octal to Decimal
int oct_dec(int octal) {
    int decimal = 0, base = 1;
    int temp = octal;
    while (temp > 0) {
        int digit = temp % 10;
        if (digit < 0 || digit > 7) {
            cout << "Invalid octal number!" << endl;
            return -1;
        }
        temp /= 10;
    }
    while (octal > 0) {
        int lastDigit = octal % 10;
        decimal += lastDigit * base;
        base *= 8;
        octal /= 10;
    }
    return decimal;
}

// Hexadecimal to Decimal
int hex_dec(string hex) {
    int decimal = 0, base = 1;
    int len = hex.length();
    for (int i = len - 1; i >= 0; i--) {
        char c = hex[i];
        int value;
        if (c >= '0' && c <= '9')
            value = c - '0';
        else if (c >= 'A' && c <= 'F')
            value = c - 'A' + 10;
        else if (c >= 'a' && c <= 'f')
            value = c - 'a' + 10;
        else {
            cout << "Invalid hexadecimal number!" << endl;
            return -1;
        }
        decimal += value * base;
        base *= 16;
    }
    return decimal;
}

int main() {
    int num, ch;
    string hex;
    cout << "\n1: dec to binary\n2: dec to oct\n3: dec to hex\n4: binary to dec\n5: oct to dec\n6: hex to dec\nEnter choice: ";
    cin >> ch;
    switch (ch) {
        case 1:
            cout << "Enter number for conversion: ";
            cin >> num;
            decimal_binary(num);
            break;
        case 2:
            cout << "Enter number for conversion: ";
            cin >> num;
            decimal_octal(num);
            break;
        case 3:
            cout << "Enter number for conversion: ";
            cin >> num;
            decimal_hex(num);
            break;
        case 4:
            cout << "Enter number for conversion: ";
            cin >> num;
            cout << binary_decimal(num) << endl;
            break;
        case 5:
            cout << "Enter number for conversion: ";
            cin >> num;
            cout << oct_dec(num) << endl;
            break;
        case 6:
            cout << "Enter number for conversion: ";
            cin >> hex;
            cout << hex_dec(hex) << endl;
            break;
        default:
            cout << "Invalid choice!" << endl;
            break;
    }
    return 0;
}
