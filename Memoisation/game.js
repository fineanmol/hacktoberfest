var gamePattern=[];
userClickedPattern=[];
var buttonColour=["red","blue","green","yellow"];
var count=0;
var ke=true;
 $(document).on("keydown",function(){
   if(ke===true)
   {
     ke=false;
     nextSequence();
   }
});
function nextSequence()
{
  $("#level-title").text("Level "+count);
  count++;
  var randomNumber=Math.floor(Math.random()*4);
  var randomChosenColor=buttonColour[randomNumber];
  gamePattern.push(randomChosenColor);
  $("#"+randomChosenColor).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
  playSound(randomChosenColor);
}
$(".btn").on("click",function(){
   var userChosenColour=this.id;
   userClickedPattern.push(userChosenColour);
   playSound(userChosenColour);
   animatePress(userChosenColour);
   checkAnswer(userClickedPattern.length-1);
});
function playSound(name)
{
    var aud= new Audio("sounds/"+name+".mp3");
    aud.play();
}
function animatePress(currentColor)
{
   $("#"+currentColor).addClass("pressed");
   setTimeout(function(){
     $("#"+currentColor).removeClass("pressed");
   },100);
}
function checkAnswer(leng)
{
  if(gamePattern[leng]===userClickedPattern[leng])
  {
    setTimeout(function(){
      if(leng==count-1)
      {
        userClickedPattern=[];
        nextSequence();
      }
    },1000);
  }
  else
  {
    var audi= new Audio("sounds/wrong.mp3");
    audi.play();
    $("body").addClass("game-over");
    setTimeout(function(){
      $("body").removeClass("game-over"),200
    });
    reset();
    $("#level-title").text("Game Over, Press Any Key to Restart");
  }
}
function reset()
{
  count=0;
  userClickedPattern=[];
  gamePattern=[];
  ke=true;
}
