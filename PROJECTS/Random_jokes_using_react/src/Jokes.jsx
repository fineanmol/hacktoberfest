import { useState,useEffect } from "react";

export default function Jokes(){
    let [joke, setJoke] = useState({});

    let URL = "https://official-joke-api.appspot.com/random_joke";
    
    const getNewJokes =  async () => {
        let response = await fetch(URL);
        let JSONresponse = await response.json();
        setJoke({setup: JSONresponse.setup, punchline: JSONresponse.punchline});
    }

    useEffect(() => {
        async function getinitialjoke() {
            let response = await fetch(URL);
            let JSONresponse = await response.json();
            setJoke({setup: JSONresponse.setup, punchline: JSONresponse.punchline});
        }
        getinitialjoke() 
    }, []);

    return (
        <div>
            <h1>joke of the day !</h1>
            <h2>{joke.setup}</h2> 
            <h2>{joke.punchline}</h2> 
            <button onClick={getNewJokes}>Generate</button>
        </div>
    );
}