function largest(num1,num2)  {

    if(num1 > num2) {
        return num1;
    } else {
        return num2;
    }

}

var num1 = 10;

var num2 = 14;

var biggestNum = largest(num1,num2);

console.log("The Largest Number Is " + biggestNum);