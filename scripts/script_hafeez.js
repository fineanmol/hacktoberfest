// ************************************************
// *   Project Name: ASCII Converter              *
// *   Contributers : Hafizur Rahman, Danish      *
// *   Date: 21-Jan-2022                          *
// ************************************************
var key = document.querySelector('#key');
var code = document.querySelector('#code');

document.addEventListener('keypress', function (e) {
  e.charCode === 32 ? (key.textContent = 'space') : (key.textContent = e.key);
  code.textContent = e.charCode;
});