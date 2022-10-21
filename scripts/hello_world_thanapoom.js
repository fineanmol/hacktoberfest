// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Thanapoom
// GITHUB: https://github.com/thanapoom21

/**
 * Create a class Person and define default name and location.
 * Create a method called sayHello that returns a template literal with string interpolation.
 * Create a new variable from Person class constructor with values.
 * Print out the string.
 */

class Person {
  constructor(name = "Anonymous", location = "Somewhere on Earth") {
    this.name = name;
    this.location = location
  }

  sayHello() {
    return `Hello, World! by ${this.name} from ${this.location}`;
  }
}

let person = new Person('Thanapoom', 'Las Vegas');

console.log(person.sayHello())