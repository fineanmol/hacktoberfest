// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Anmol Agarwal
// GITHUB: https://github.com/fineanmol
// LINK: http://es6-features.org/

var Person = function (name, location) {
  this.name = name ? name : "Anyonymous";
  this.place = location ? location : "USA";
};

Person.prototype.greeting = function (name) {
  name = name ? name : this.name;
  var str = "Hello, World! by " + name;
  console.log(str);
  return str;
};

// Javascript ES6
class Person {
  constructor(name = "Anyonymous", location = "USA") {
    this.name = name;
    this.place = location;
  }
  greeting(name = this.name) {
    let str = "Hello, World! by " + name;
    console.log(str);
    return str;
  }
}

var myself = new Person("Tyler", "USA");
myself.greeting();
