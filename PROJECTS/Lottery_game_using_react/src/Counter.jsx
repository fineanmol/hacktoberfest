import { useState,useEffect } from "react";

export default function Counter(){
    let [count, setCount1] = useState(0);
    let [countdec, setCount2] = useState(0);
    
    useEffect(function printSomething(){
        console.log("This is a side effect !");
    }, [countdec]);

    return (
        <div>
            <h2>Increase count here</h2>
            <h1>Count = {count}</h1>
            <button onClick={() => setCount1(count+1)}>+1</button>
            <hr/>
            <h2>Decrease count here</h2>
            <h1>Count = {countdec}</h1>
            <button onClick={() => setCount2(countdec-1)}>-1</button>
        </div>
        
    );
}