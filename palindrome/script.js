const form = document.getElementById('pal-form');
const input = document.getElementById('text');
const result = document.getElementById('result');
const clearBtn = document.getElementById('clearBtn');

function normalize(s){
  return s.replace(/[^0-9a-z]/gi, '').toLowerCase();
}

function isPalindrome(s){
  const n = normalize(s);
  let i = 0, j = n.length - 1;
  while(i < j){
    if(n[i] !== n[j]) return false;
    i++; j--;
  }
  return true;
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if(!text){
    result.hidden = false;
    result.textContent = 'Please enter some text.';
    return;
  }
  const yes = isPalindrome(text);
  result.hidden = false;
  result.textContent = yes ? `"${text}" is a palindrome.` : `"${text}" is NOT a palindrome.`;
});

clearBtn.addEventListener('click', () => {
  input.value = '';
  result.hidden = true;
  input.focus();
});
