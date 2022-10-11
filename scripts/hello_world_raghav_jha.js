// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Raghav Jha
// GITHUB: https://github.com/jharaghav32

// This hello world uses Javascript Objects and Classes.
// Creates a Person object using a Constructor function and a method greeting() that logs out and returns a greeting string.
// Written in ES5 and ES6 versions of Javascript. Comment out one of the versions before running.



var Person = function(name,location){
    this.name = (name) ? name : "Unknown";
    this.place = (location) ? location : "India";
  }
  
  Person.prototype.greeting = function(name){
    name = (name) ? name : this.name;
    var str = "Hello, Everyone! by " + name;
    console.log(str);
    return str;
  }
  
  // Javascript ES6
  class Person {
    constructor (name='Unknown', location='India') {
      this.name = name;
      this.place = location;
    }
    greeting (name=this.name) {
      let str = "Hello, Everyone! by " + name;
      console.log(str);
      return str;
    }
  }
  
  var myself = new Person('Raghav','India');
  myself.greeting();