import React from 'react';
import axios from 'axios';

function Exercises(){
    const [exercises , setExercises] = useState([])
    
   
      async function Main () {
       const {data} = await axios.get('http://127.0.0.1:5555/exercises')
       setExercises(data)
       }
   useEffect(() => {Main()}, [])
      
   
   
   
   return ( <>

       <div className="container">

           {exercises.map((exercise ,index ) => (
             <div key={exercise.id} className="card" style={{ width: "18rem" }}>
                <div className="card-body">
               <h1 className="card-title">{exercise.name}</h1>
               <h2 className="card-text">{exercise.type}</h2>
               <p className="card-text">{exercise.muscle}</p>
               <p className="card-text">{exercise.equipment}</p>
               <p className="card-text">{exercise.difficulty}</p>
               <p className="card-text">{exercise.instructions}</p>
             </div>
           </div>))}
       </div>
   
   
   </> )
   
   }
   
   
   export default Exercises


