const canvasEl = document.querySelector("canvas");
const canvasContext = canvasEl.getContext("2d");

// var background = new Image();
// background.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx3rh-5p7tCEWYVt6-79ra4UmgfHQKRsYNxg&usqp=CAU";

// background.onload = function(){
//     canvasContext.drawImage(background,0,0);   
// }

canvasEl.height = window.innerHeight;
canvasEl.width = window.innerWidth;

const starcount = 1000 ;
const starsColors = "#c7c8c7";
const size = 0.004 ;
const speed = 0.04 ;

let stars = [] ;
let starSpeed = speed*canvasEl.width;
let horizontalVelocity = starSpeed*randomSign()*Math.random();
let verticalVelocity =  Math.sqrt(Math.pow(starSpeed,2)-Math.pow(horizontalVelocity,2));


for( let i = 0 ; i<starcount ; i++)
{
     let speedBoost = Math.random()*2.5 + 0.5 ;
    stars[i]=
    {
        radius : (Math.random()*size*canvasEl.width)/2,
        horizontalPosition : Math.random()*canvasEl.width ,
        verticalPosition : Math.random()*canvasEl.height ,
        horizontalVelocity : horizontalVelocity*speedBoost ,
        verticalVelocity : verticalVelocity*speedBoost 
          
    }
   
}

let timeDiff , timeLast = 0 ;
requestAnimationFrame(runstars)

function runstars(timeNow)
{
   canvasContext.clearRect(0,0,canvasEl.width , canvasEl.height);
   timeDiff = timeNow - timeLast ;
   timeLast = timeNow ;

   canvasContext.fillStyle = starsColors ; 
   for(let i = 0 ; i< starcount ; i++)
   {
    canvasContext.beginPath();
    canvasContext.arc(stars[i].horizontalPosition , stars[i].verticalPosition ,stars[i].radius ,0 , Math.PI*2)


    canvasContext.fill(); 

    stars[i].horizontalPosition += stars[i].horizontalVelocity*timeDiff*0.001;


    if(stars[i].horizontalPosition<0 - stars[i].radius)
    {
        stars[i].horizontalPosition = canvasEl.width + stars[i].radius ;
    }
    else if(stars[i].horizontalPosition + stars[i].radius > canvasEl.width)
    {
        stars[i].horizontalPosition = 0
    }


    stars[i].verticalPosition += stars[i].verticalVelocity*timeDiff*0.001;

    if(stars[i].verticalPosition<0 - stars[i].radius)
    {
        stars[i].verticalPosition = canvasEl.height + stars[i].radius ;
    }
    else if(stars[i].verticalPosition + stars[i].radius > canvasEl.height)
    {
        stars[i].verticalPosition = 0
    }


    stars[i].verticalPosition += stars[i].verticalVelocity*timeDiff*0.001;

   }
   

  

   requestAnimationFrame(runstars); 

}

function randomSign()
{
    return Math.random() > 0.5 ? 1 : -1;
};

