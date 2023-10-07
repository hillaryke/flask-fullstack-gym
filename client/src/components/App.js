import React from 'react';
import { Switch, Route } from "react-router-dom";
import Signup from "./Signup";
import Signin from "./Signin";
import Exercises from "./Exercises"; // Import the component you want to render

function App() {
  return (
    <div>
      <main>
        <Switch>
          <Route exact path="/exercises">
            <Exercises />
          </Route>
          <Route exact path="/signin">
            <Signin />
          </Route>
          <Route exact path="/signup">
            <Signup />
          </Route>
          {/* Replace <Home /> with the component you want to render */}
          <Route exact path="/">
            <Exercises /> {/* Replace with the desired component */}
          </Route>
        </Switch>
      </main>
    </div>
  );
}

export default App;
