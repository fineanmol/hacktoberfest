import './App.css'
import Lottery from "./Lottery.jsx"

function App() {
   let winningCondition = (ticket) => {
     return ticket.every((num) => num != 0 && num === ticket[0]);
   }
 
  return (<> <Lottery n ={3} winningCondition={winningCondition}/></>);
}

export default App
