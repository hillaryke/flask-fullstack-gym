import { Switch, Route } from "react-router-dom";
import Signup from "./Signup";
import Signin from "./Signin";
import Exercises from "./Exercises";

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
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>
      </main>
    </div>
  );
}

export default App;
