

var arr = [
    {
        "que": "What is 2+2 ?",
        "a": "4",
        "b": "5",
        "c": "7",
        "d": "9",
        "correctans": "a"

    },
    {
        "que": "What is 4 + 4 ?",
        "a": "4",
        "b": "5",
        "c": "8",
        "d": "9",
        "correctans": "c"

    },
    {
        "que": "What is 8 + 8 ?",
        "a": "4",
        "b": "5",
        "c": "8",
        "d": "16",
        "correctans": "d"

    },
    {
        "que": "Which is a Markup language ?",
        "a": "HTML",
        "b": "Javascript",
        "c": "php",
        "d": "Java",
        "correctans": "a"

    },
    {
        "que": "How javascript works ?",
        "a": "Synchronously",
        "b": "Asynchronously",
        "c": "Line by line",
        "d": "None of the above",
        "correctans": "b"

    },
    {
        "que": "Which one is framwork of javascript ?",
        "a": "React",
        "b": "Springboot",
        "c": "Flask",
        "d": "Django",
        "correctans": "a"

    },
    {
        "que": "Which type of framework nodejs is ?",
        "a": "Frontend",
        "b": "Backend",
        "c": "Both",
        "d": "None of the above",
        "correctans": "b"

    },
    {
        "que": "Which one is framework of nodejs ?",
        "a": "Expressjs",
        "b": "Flask",
        "c": "Hadoop",
        "d": "Django",
        "correctans": "a"

    },
    {
        "que": "Which one of the language has fast execution time ?",
        "a": "Java",
        "b": "C++",
        "c": "C",
        "d": "Python",
        "correctans": "b"

    },
    {
        "que": "Which one of the data structure has pop,push function ?",
        "a": "Linkedlist",
        "b": "Stack",
        "c": "Queue",
        "d": "Hashmap",
        "correctans": "b"

    }

];
var time = document.querySelector(".time");

var count = 0;



var ques = document.querySelector(".question");
var index = 0;
var optioninput = document.querySelectorAll("#options");
if (index == 0 || index > 0) {
    setInterval(() => {
        countinc();
    }, 1000);
}
function Loadques() {

    if (index == arr.length) {
        end();
    }
    else {
        var data = arr[index];
        ques.innerText = data.que;
        optioninput[0].nextElementSibling.innerHTML = data.a;
        optioninput[1].nextElementSibling.innerHTML = data.b;
        optioninput[2].nextElementSibling.innerHTML = data.c;
        optioninput[3].nextElementSibling.innerHTML = data.d;
    }

}

Loadques()
/*question load up*/
var right = 0, wrong = 0;
function loadup() {
    var data = arr[index];
    index++;
    console.log(data);
    var ans = getanswer(); /*answer fetched from get anwser*/
    
    if (ans == data.correctans) {
        right++;
        count = 0;
        setTimeout(() => {
            countinc();
        }, 100);
        reset();
        console.log("Right is" + right);
        // data++;
    } else if (ans != data.correctans) {
        wrong++;
        count = 0;
        setTimeout(() => {
            countinc();
        }, 100);

        console.log(`Wrong is ${wrong}`);
    }

    console.log(`index is ${index}`);
    Loadques();
}

var getanswer = () => {
    var answer;
    optioninput.forEach(
        (input) => {
            if (input.checked) {
                console.log("Yes");
                answer = input.value;
            }
        }
    )
    return answer; /* will return value to loadup*/

}
function end() { /*end of question */
    document.querySelector(".container").innerHTML = `Well done, <br>Thanks for playing <br> ${right}/${wrong}`
    if(wrong>right){
        document.querySelector(".container").innerHTML = `Better luck next time, <br> thanks for playing, <br> ${right}/${wrong}`

    }
}


var reset = () => {
    optioninput.forEach((input) => {
        input.checked = false;
    })
}
function countinc() {


    count += 1;
    time.innerHTML = `Time remaining: ${count}`;
    if (count == 15) {
        loadup();
        count = 0;
    }

}

function Rules(){
    document.body.innerHTML = `Welcome to <strong>TRAIN YOUR BRAIN </strong>`;
}

