import { useState } from "react";
import { genTicket, /*sum*/} from "./helper";
import Ticket from "./Ticket";
import "./Lottery.css";
import Btn1 from "./Btn1";
import Btn2 from "./Btn2";
import Result from "./Result";

export default function Lottery({n, winningCondition}) {
  let[ticket, setTicket] = useState(genTicket(n));
  let isWinning = winningCondition(ticket);
  let buyTicket = () =>{
    setTicket(genTicket(n));
  };
  let initiallyzeroes = () =>{
    setTicket(Array(n).fill(0)); 
  };
  return (
    <div>
      <h1>Lottery game ! </h1>
          <div className="ticket" style={{backgroundColor: isWinning ? "white":"black",color: isWinning ? "black":"white"}}>
            <Ticket ticket={ticket}/>
          </div>
          <Result isWinning={isWinning}/>
          <Btn1 action={buyTicket}/>
          <Btn2 action={initiallyzeroes}/>
          
    </div>
  );
}