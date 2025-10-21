function genTicket(n){ //n - size of array for here its 3
  let arr = new Array(n);
  for(let i=0; i<n;  i++){
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
}

function sum(arr){
  let total = 0;  
  arr.forEach(num=> total+=num);
    return total;
}

export {genTicket, sum};