let phrase = "Hello, World! Happy Hacktoberfest";
const words = phrase.split(" ")
let maxLength = 0
words.forEach(word => {
  if (word.length > maxLength) {
    maxLength = word.length
  }
});

console.log('*'.repeat(maxLength + 4));

words.forEach(word =>
  console.log("* " + word + ' '.repeat(maxLength - word.length) + ' *')

);

console.log('*'.repeat(maxLength + 4));
