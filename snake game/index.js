// game variables
var score =0;
var moveDirection = {x:0,y:0};
var eating = new Audio("snake_eat.mp3");
var gameover=new Audio("gameover.mp3");
var movement=new Audio("move.mp3");
var lastRenderTime=0;
var timeInterval=0.2;
var snakeArray = [ // snakeArray is an array of snake with starting position 5,9 in grid system
  {x:10 , y:17}
]
var foodPosition={x:4, y:7};
// game function
function main(RealTime){// Here the RealTime will tell the time in milliseconds for each recursive call
  window.requestAnimationFrame(main);// recursion of main function
  //console.log(RealTime);
  if((RealTime-lastRenderTime)/1000 < timeInterval){ // render the changes only if the timeInterval betweent two function calling is 0.5 seconds
    return;// we divide (RealTime-lastRenderTime) by 1000 to measure it in seconds
  }
  lastRenderTime=RealTime;
  gameEngine();// calling gameEngine function
}
function isCollide(snake){
  for(var i=1;i<snakeArray.length;i++){
    if(snake[0].x===snake[i].x && snake[0].y===snake[i].y){
      return true;
    }
    else if (snake[i].x>=18 || snake[i].y>=18 || snake[i].x<=0 || snake[i].y<=0){
      return true;
    }
    else{
      return false;
    }
  }
}
function gameEngine(){
  // part 1: updating the snake array and food
 if (isCollide(snakeArray)){
   gameover.play();
   moveDirection={x:0 , y:0};

   window.addEventListener("keydown",function(){
     tag.innerHTML("Game Over!!! Press any key to restart");
     location.reload()
   });
   snakeArray=[{x:7,y:9}];
   score=0;
 }
 // if the snake eats the food increment the size of snake and regenerate the food at another location
 if(snakeArray[0].x===foodPosition.x && snakeArray[0].y===foodPosition.y){
     snakeArray.unshift({x: snakeArray[0].x+moveDirection.x , y: snakeArray[0].y+moveDirection.y});
     eating.play();
   //regenerating food at another location

   let a = 2;
   let b = 16;
   foodPosition = {x: Math.round(a + (b-a)* Math.random()), y: Math.round(a + (b-a)* Math.random())}

 }
// to move the body as the head is moving
for (var i = snakeArray.length-2; i >=0; i--) {

  snakeArray[i+1]={...snakeArray[i]};// the reason we use {...snakeArr[i]} instead of snakeArr[i] is because of reference pointing
}
snakeArray[0].x+=moveDirection.x;
snakeArray[0].y+=moveDirection.y;
  //part 2: displaying and updating the snake


  background.innerHTML=""; // this line is used to avoid multiple snakes

//displaying snake
  snakeArray.forEach((e,index)=>{ // This will perform particular line of code for all elements of snakeArray iterating through index of the element object 'e'
    snakeElement = document.createElement('div');// creating a new elements
    snakeElement.style.gridRowStart=e.y;
    snakeElement.style.gridColumnStart=e.x;
    if(index === 0){
      snakeElement.classList.add('head');
    }
    else{
    snakeElement.classList.add('body');
  }
    background.appendChild(snakeElement); // snakeElement is appended inside background class
  })
//displaying food
foodElement=document.createElement('div');
foodElement.style.gridRowStart=foodPosition.y;
foodElement.style.gridColumnStart=foodPosition.x;
foodElement.classList.add('food');
background.appendChild(foodElement);
}


// Main logic starts here
window.requestAnimationFrame(main); //requestAnimationFrame is used for game animation and this function is similar to setInterval function
window.addEventListener('keydown',e =>{
   moveDirection={x:0,y:1};// Starting the game , the snake starts to move towards down since y=1
   movement.play();
   switch (e.key) {
     case "ArrowDown":
       console.log("ArrowDown");
       moveDirection.x=0;
       moveDirection.y=1;
       break;
    case "ArrowUp":
      console.log("ArrowUp");
      moveDirection.x=0;
      moveDirection.y=-1;
      break;
    case "ArrowRight":
       console.log("ArrowRight");
       moveDirection.x=1;
       moveDirection.y=0;
       break;
    case "ArrowLeft":
        console.log("ArrowLeft");
        moveDirection.x=-1;
        moveDirection.y=0;
       break;
     default:
       console.log("incorrect key pressed");
   }
});
window.requestAnimationFrame(main);
