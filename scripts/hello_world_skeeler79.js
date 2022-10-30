function sayHello(alphabet) {
    
    let helloArr = [];
    helloArr.push(alphabet.charAt(7));
    helloArr.push(alphabet.charAt(4));
    helloArr.push(alphabet.charAt(11));
    helloArr.push(alphabet.charAt(11));
    helloArr.push(alphabet.charAt(14));
    helloArr.push(alphabet.charAt(28));
    helloArr.push(alphabet.charAt(22));
    helloArr.push(alphabet.charAt(14));
    helloArr.push(alphabet.charAt(17));
    helloArr.push(alphabet.charAt(11));
    helloArr.push(alphabet.charAt(3));
    helloArr.push(alphabet.charAt(27));


    return helloArr.join('');


}

console.log(sayHello('abcdefghijklmnopqrstuvwxyz,! '))