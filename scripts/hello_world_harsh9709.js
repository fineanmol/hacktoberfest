// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Harshit Kumar Vishwakarma
// GITHUB: https://github.com/harsh9709



// used object literal and this concept to log "hello world" by calling the function inside the object

const greeting={
    name:"Harshit",
    greet:"Hello World!",
    final_msg:function(){
        console.log(`${this.greet} by ${this.name}`);
    }
}

greeting.final_msg()