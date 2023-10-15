import logo from './logo.svg';
import './App.css';
import {useEffect} from "react";

function App() {
    const [members, setMembers] = useState([{}]);

    useEffect(() => {
        fetch('http://localhost:5555/signup', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        }).then(response => {
            console.log(response);
            return response.json();
        }).then(data => {
            setMembers(data);
        });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default App;
