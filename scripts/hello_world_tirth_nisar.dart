// LANGUAGE: Dart
// ENV: Dart SDK
// AUTHOR: Tirth Nisar
// GITHUB: https://github.com/TirthNisar193

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
