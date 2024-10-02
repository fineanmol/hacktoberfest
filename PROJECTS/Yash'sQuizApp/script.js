/*

questions =
[
 {
    question : " question goes here" ,
    answer : [
                {text : option 1 , }
             ]
    
             
 }

]

step 0. create a central function {

        call =>  loadFn( currentIndex ) ;

}



step 1. load question and its options
 {
        first this function will remove all the children of " answer-buttons"
        then it will generate the question and its options according to current
        index


 }
step 2. when clicked on any 1 option
  {
        make other options unclickable
        make the selection green if true else red
        the next button should appear 
        and increase the score by 1 if true else continue
  } 
step 3. Add functionality for next button when it is clicked
  {     
        increase the current index : currentIndex++;

        call => load(currentindex);
        run the load function to load the next question and options
        also when at the last index instead of calling the load function call the " show result function " to show the result 
  }

*/

// 10 questions 
const questions =[
    {
        question:"What is the full form of CSS ?",

        answers:[
            {text : "Cute Style Sheets" , correct : false},
            {text : "Clear Style Sheets" , correct : false},
            {text : "Cascading Styles Sheet" , correct : false},
            {text : "Cascading Style Sheets" , correct : true},
        ],

        
    },
    {
    question: "What does HTTP stand for?",
    answers: [
      { text: "Hypertext Transfer Protocol", correct: true },
      { text: "Hypertext Transfer Program", correct: false },
      { text: "Hightext Transfer Protocol", correct: false },
      { text: "Hyper Transfer Text Protocol", correct: false },
    ],
  },
  {
    question: "Which programming language is known as the backbone of the web?",
    answers: [
      { text: "Python", correct: false },
      { text: "JavaScript", correct: true },
      { text: "Ruby", correct: false },
      { text: "Java", correct: false },
    ],
  },
  {
    question: "Which HTML element is used to include JavaScript code?",
    answers: [
      { text: "<js>", correct: false },
      { text: "<script>", correct: true },
      { text: "<javascript>", correct: false },
      { text: "<code>", correct: false },
    ],
  },
  {
    question: "What is the primary function of an API?",
    answers: [
      { text: "Storing data", correct: false },
      { text: "Creating a database", correct: false },
      { text: "Enabling communication between applications", correct: true },
      { text: "Designing websites", correct: false },
    ],
  },
  {
    question: "Which of the following is a NoSQL database?",
    answers: [
      { text: "PostgreSQL", correct: false },
      { text: "MySQL", correct: false },
      { text: "MongoDB", correct: true },
      { text: "Oracle", correct: false },
    ],
  },
  {
    question: "What does 'SEO' stand for in web development?",
    answers: [
      { text: "Search Engine Optimization", correct: true },
      { text: "Social Engagement Operations", correct: false },
      { text: "Search Extension Online", correct: false },
      { text: "Systematic Engine Optimization", correct: false },
    ],
  },
  {
    question: "Which company developed the React framework?",
    answers: [
      { text: "Google", correct: false },
      { text: "Microsoft", correct: false },
      { text: "Facebook", correct: true },
      { text: "Apple", correct: false },
    ],
  },
  {
    question: "What does 'GPU' stand for?",
    answers: [
      { text: "Global Processing Unit", correct: false },
      { text: "Graphics Processing Unit", correct: true },
      { text: "Graphical Programming Unit", correct: false },
      { text: "General Processing Unit", correct: false },
    ],
  },
  {
    question: "Which of the following is a JavaScript framework?",
    answers: [
      { text: "Angular", correct: true },
      { text: "Django", correct: false },
      { text: "Laravel", correct: false },
      { text: "Rails", correct: false },
    ],
  },
]

const answerContainer = document.querySelector("#answer-buttons");
const displayQuestion = document.querySelector("#question");
let score = 0;
let currentIndex = 0;
const nextButton = document.querySelector("#next-btn")
const result = document.querySelector(".result")
resultTextContent = document.querySelector(".result h1")
const retryButton = document.querySelector(".retry");

nextButton.addEventListener("click",() => {
    nextFn();
})
retryButton.addEventListener("click",()=>{
  score=0;
  currentIndex=0;
  result.classList.add("hide");
  startQuiz();
})

//Function to start the quiz
function startQuiz(){
    loadFn(currentIndex);
}

//Function to load question and options
function loadFn(currentIndex){
    //Deleting the previous options
     removeFn();
    
    //loading question according to index number
    displayQuestion.textContent=questions[currentIndex].question;

    //creating new options
    questions[currentIndex].answers.forEach((e) => {
        
        const options = document.createElement("button");
        options.textContent = e.text;
        options.classList.add("btn");
        answerContainer.appendChild(options);
        options.addEventListener("click",() => {
           if(e.correct == true){
            options.classList.add("correct");
            score++;
            console.log("Added class: correct");
           }
           else{
            options.classList.add("incorrect");
            console.log("Added class: incorrect");
           }
           nextButton.classList.remove("hide");
           answerContainer.classList.add("disable")
           
        })
    })

}

//Function to remove previous options
function removeFn(){
    //removing previous options
    Array.from(answerContainer.children).forEach((e) => {
        answerContainer.removeChild(e);
    });
}

//Funtion for updation
function nextFn(){
    currentIndex++;
    answerContainer.classList.remove("disable");
    nextButton.classList.add("hide");
    if(currentIndex==3){
        showResult();
    }
    else{
        startQuiz();
    }
}

function showResult(){
    resultTextContent.textContent = `Your Score is ${score}/10`
    result.classList.remove("hide");
}
startQuiz();