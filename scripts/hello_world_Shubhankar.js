// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Shubhankar Nautiyal
// GITHUB: https://github.com/Shubhankar-1
// LINK: http://es6-features.org/

// This hello world uses Javascript Objects and Classes.
// Creates a Person object using a Constructor function and a method greeting() that logs out and returns a greeting string.


// Javascript ES6
class Person {
    constructor(name = "Shubhankar", location = "India") {
        this.name = name;
        this.place = location;
    }
    greeting(name = this.name) {
        let str = "Hello, World! by " + name;
        console.log(str);
        return str;
    }
}

var myself = new Person("Shubhankar", "India");
myself.greeting();
