// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Shubham verma
// GITHUB: https://github.com/shubham1091

class Person {
    constructor(name) {
        this.name = name;
    }
    greetingTo(name){
        return `Hi ${name}, ${this.name} this side Nice to meet you`;
    }
}

const myself = new Person("shubham");
console.log(myself.greetingTo("Anmol"))