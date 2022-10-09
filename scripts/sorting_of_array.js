
// program to sort the elements of an array

let arr = [3, 5, 2, 9, 34, 18, 1, 8];

arr.sort(function(a,b){
    if(a > b)
        return 1;
    else if(a < b)
        return -1;
    else
        return 0;
});

console.log(arr);

