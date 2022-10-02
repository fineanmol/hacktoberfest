// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Anmol Agarwal
// GITHUB: https://github.com/fineanmol
// LINK: http://es6-features.org/

// This hello world uses Javascript Objects and Classes.
// Creates a Person object using a Constructor function and a method greeting() that logs out and returns a greeting string.
// Written in ES5 and ES6 versions of Javascript. Comment out one of the versions before running.
// Try it for yourself here, https://replit.com/join/sfikpxhxll-fineanmol


// Javascript ES5
var Person = function(name,location){
  this.name = (name) ? name : "Anyonymous";
  this.place = (location) ? location : "USA";
}

Person.prototype.greeting = function(name){
  name = (name) ? name : this.name;
  var str = "Hello, World! by " + name;
  console.log(str);
  return str;
}

// Javascript ES6
class Person {
  constructor (name='Anyonymous', location='USA') {
    this.name = name;
    this.place = location;
  }
  greeting (name=this.name) {
    let str = "Hello, World! by " + name;
    console.log(str);
    return str;
  }
}

var myself = new Person('Anmol','UK');
myself.greeting();
