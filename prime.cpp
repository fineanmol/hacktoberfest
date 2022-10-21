#include <iostream>
using namespace std;

int main() {

  int i, positive;
  bool is_prime = true;

  cout << "Enter a positive integer: ";
  cin >> positive;

  if (positive == 0 || positive == 1) {
    is_prime = false;
  }

  // lcheck if a number is positive
  for (i = 2; i <= positive/2; ++i) {
    if (positive % i == 0) {
      is_prime = false;
      break;
    }
  }

  if (is_prime)
    cout << positive << " is a prime number";
  else
    cout << positive << " is not a prime number";

  return 0;
}
