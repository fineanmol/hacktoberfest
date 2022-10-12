const data = [
  72, 101, 108, 108, 111,
  32, 87, 111, 114, 108,
  100, 33
];

console.log(data.map((code) => String.fromCharCode(code)).join(''));