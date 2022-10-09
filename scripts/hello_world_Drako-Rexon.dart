// LANGUAGE: Dart
// ENV: Dart SDK
// AUTHOR: Abhishek Kayal
// GITHUB: https://github.com/Drako-Rexon

class printingHello {
  String hello = "";

  printingHello(String obj) {
    hello = obj;
  }

  void printHello() {
    print(hello);
  }
}

void main() {
  printingHello("Hello world").printHello();
}
