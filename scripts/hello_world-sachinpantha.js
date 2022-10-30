//This is the simples way to generate fibonacci sequence using vanilla js
let a = 0;
let b = 1;
for (i = 0; i < 5; i++) {
    [a, b] = [b, a + b]
    console.log(a)
}