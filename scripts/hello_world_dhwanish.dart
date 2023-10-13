// LANGUAGE: Dart
// ENV: Dart SDK
// AUTHOR: Dhwanish
// GITHUB: https://github.com/dhwanish-3

class printingHello {
  String? hello;

  printingHello({required this.hello});

  void printHello() {
    print(hello);
  }
}

void main() {
  printingHello(hello: "Hello world").printHello();
}
