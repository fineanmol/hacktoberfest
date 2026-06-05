/*This is the popular quetion leeding to lanthier solution.
Contributed by Sonu Kushwaha*/
#include <iostream>
#include <string>
using namespace std;

// Function for implementing of Function:
string intToRoman(int num)
{
    string ones[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    string tens[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    string hrns[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    string ths[] = {"", "M", "MM", "MMM"};

    return (ths[num / 1000] + hrns[(num % 1000) / 100] + tens[(num % 100) / 10] + ones[num % 10]);
}

// main program
int main()
{
    int n = 24;

    cout << "Enter number ot be converted:";
    cin >> n;
    cout << intToRoman(n) << endl;
    // calling the TOH

    return 0;
}
