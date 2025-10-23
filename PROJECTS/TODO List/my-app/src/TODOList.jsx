import { use, useState } from "react";
import { v4 as uuidv4 } from 'uuid';

 export default function TodoList(){
    let [todos, setTodos] = useState([{task : "sample-task", id: uuidv4(), isDone : false}]);
    let [newTodo, setNewTodo] = useState("");

    let  addnewTask = () => {
      setTodos( (prevTodos)=> {
        return [...prevTodos, {task : newTodo, id:uuidv4(), isDone: false}]

    }); 
      setNewTodo("");
    }

    let updateTodoValue = (event) => {
        setNewTodo(event.target.value);
    }

    let deleteTodo = (id)=> {
          setTodos((prevTodos)=> todos.filter((prevTodos)=> prevTodos.id != id));     
    }

    let markAllDone =() =>{
      setTodos((prevTodos)=> 
        prevTodos.map((todo) => {
        return {
            ...todo,
            isDone: true,       
        };
      })   
    )
    }
    let markAsDone =(id) =>{
      setTodos((prevTodos)=>  
        prevTodos.map((todo) => {
          if(todo.id == id){
        return {
            ...todo,
           isDone : true,
        };
      }
      else {
        return todo;
      }
      })
    )  
    }
    
  
    return (
        <div>
        <input placeholder="Add a Task" value={newTodo} onChange={updateTodoValue} style={{ padding: "10px", width: "250px" }}></input>
         <br></br>
        <button type="button" onClick={addnewTask} style={{ padding: "10px 20px", cursor: "pointer", marginTop:"20px" ,backgroundColor:"blueviolet" }}>Add Task</button>
        <br></br><br></br><br></br>
        <hr style={{ marginTop: "2px" }}></hr>                                                                          
            <h4>Tasks Todo</h4>
            <ul style={{ listStyleType: "none"}}>
                {todos.map((todo) => (
                 <li key={todo.id} style={{ margin: "10px 0", backgroundColor:"royalblue",padding:"0 20px 0 20px"}}>
                <span style={todo.isDone ? {textDecorationLine : "line-through"} : {}}> {todo.task} </span>
                &nbsp; &nbsp; &nbsp; 
                <button onClick={() =>  deleteTodo(todo.id)} style={{ margin:"10px",padding: "10px 20px", cursor: "pointer", marginTop:"20px" ,backgroundColor:"silver" }} >Delete</button>
                <button onClick={() =>  markAsDone(todo.id)}  style={{ padding: "10px 20px", cursor: "pointer", marginTop:"20px" ,backgroundColor:"skyBlue" }}>Mark As Done</button>
                 </li>
                ))}
            </ul>
            <br></br>
            <button onClick={markAllDone} style={{backgroundColor:"palegreen"}}>Mark All As Done</button>
        </div>
    )
 }