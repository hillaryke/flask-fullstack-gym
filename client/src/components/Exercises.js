import React, {useState,useEffect} from 'react';
import axios from '../api/axios';

function Exercises(){
    const [exercises , setExercises] = useState([])
    
   
      async function Main () {
       const {data} = await axios.get('http://127.0.0.1:5555/exercises')
       setExercises(data)
       }
   useEffect(() => {Main()}, [])
      
   
   
   
   return ( <>

     <div className="container">
      <div className='crd-group'>
           {exercises.map((exercise ,index ) => (
             <div key={exercise.id} className="card" style={{ width: "18rem" , display: "flex" , flexDirection: "column" , flexFlow: "wrap"}}>
                <div className="card-body">
               <h1 className="card-title">NAME: {exercise.name}</h1>
               <h2 className="card-text">TYPE: {exercise.type}</h2>
               <p className="card-text">MUSCLE: {exercise.muscle}</p>
               <p className="card-text">EQUIPMENT: {exercise.equipment}</p>
               <p className="card-text">DIFFICULTY: {exercise.difficulty}</p>
               <button></button>
             </div>
           </div>))}
           </div>
       </div> 
   
   
   </> )
   
   }
   
   
   export default Exercises
