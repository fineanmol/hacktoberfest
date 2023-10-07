// LANGUAGE: Typescript
// ENV: Node.js
// AUTHOR: Bhavesh Kothari
// GITHUB: https://github.com/bkj281

interface Name {
  message: string
}

const displayMessage = (name: Name): string => {
  return `${name.message}`;
}

console.log(displayMessage({message: "Hello World!"}));