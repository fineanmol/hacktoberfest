'use-strict';

//grabing each elements
const hour = document.getElementById("hour");
const minute = document.getElementById("minute");
const second = document.getElementById("second");


const userHour = document.getElementById("user-hour");
const userMinute = document.getElementById("user-minute");
const userSecond = document.getElementById("user-seconds");


const ulList = document.getElementById("list-item")


//grabing buttons
const startBtn = document.getElementById("start-btn");
const stopBtn = document.getElementById("stop-btn");
const restartBtn = document.getElementById("restart-btn");
const addBtn = document.getElementById("add-btn")

function restart(){
   
    hour.innerHTML = 0;
    minute.innerHTML = 0;
    second.innerHTML = 0;
    userHour.value = null;
    userMinute.value = null;
    userSecond.value = null;
    ulList.innerHTML = null;
    
}

//start function
let timer;
let secondsTime = parseInt(second.innerHTML);
let minuteTime = parseInt(minute.innerHTML);
let hourTime = parseInt(hour.innerHTML);
function start(){
    
    

    timer = setInterval(()=>{
       
        if(secondsTime === 0 && minuteTime === 0 && hourTime === 0){
            clearInterval(timer);
        }
        else{

            if(secondsTime > 0){
                secondsTime--;
                second.innerHTML = secondsTime;
            }
            else{
                secondsTime = 60;
                second.innerHTML = secondsTime;
                if(minuteTime > 0){
                    minuteTime--;
                    minute.innerHTML = minuteTime;
                }
                else{
                    minuteTime = 60;
                    minute.innerHTML = minuteTime;
                    hourTime--;
                    hour.innerHTML = hourTime;
                }

        }
      

        }
    },1000)

}

//stop function
function stop(){
    clearInterval(timer);
    let li = document.createElement("li");
    li.innerHTML = `Time stamp - ${hourTime} hour : ${minuteTime} minute : ${secondsTime} seconds `;
    ulList.appendChild(li);
}


//function add
function add(e){
    e.preventDefault();
    console.log(userHour.value);
    ulList.innerHTML = "";
     secondsTime = parseInt(userSecond.value) || 0;
     second.innerHTML = secondsTime;
     minuteTime = parseInt(userMinute.value) || 0;
     minute.innerHTML = minuteTime;
     hourTime = parseInt(userHour.value) || 0;
     hour.innerHTML = hourTime;

     userHour.value = null;
     userMinute.value = null;
     userSecond.value = null;
}



startBtn.addEventListener("click",start);
stopBtn.addEventListener("click",stop);
restartBtn.addEventListener("click",restart);
addBtn.addEventListener("click",add);