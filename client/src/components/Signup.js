import React,{useState, useEffect} from 'react';
import axios from '../api/axios';
import "./Signup.css"

function Signup() {
    const initialValues = {
        username: "",
        email: "",
        phone_number : "",
        password: "",
        confirmPassword: "",
    };
    const [formValues, setFormValues] = useState(initialValues);
    const [formErrors, setFormErrors] = useState({});
    const [isSubmit, setIsSubmit] = useState(false);
    const [token , setToken] = useState("")
    
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormValues({ ...formValues, [name]: value });
    };
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormErrors(validate(formValues));
        setIsSubmit(true);

        try {
            const response = await axios.post('/signup', formValues);
            console.log('Form submission successful', response.data);
         } catch (error) {
            console.error('Error submitting form', error);
         }
    };
    
    useEffect(() => {
        console.log(formErrors);
        if (Object.keys(formErrors).length === 0 && isSubmit) {
            console.log(formValues);
        }
    }, [formErrors, formValues, isSubmit]);
    const validate = (values) => {
        const errors = {};
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;
        if (!values.username) {
            errors.username = "Username is required!";
        }
        if (!values.email) {
            errors.email = "Email is required!";
        } else if (!regex.test(values.email)) {
            errors.email = "This is not a valid email format!";
        }
        if (!values.password) {
            errors.password = "Password is required";
        } else if (values.password.length < 4) {
            errors.password = "Password must be more than 4 characters";
        } else if (values.password.length > 10) {
            errors.password = "Password cannot exceed more than 10 characters";
        }
        if (values.password !== values.confirmPassword) {
            errors.confirmPassword = "Those passwords didn’t match. Try again.";
        }
        if (!values.phone_number){
            errors.phone_number = "Phone Number is required";
        } 
        return errors;
    };
    
    return (
        <>
            <div className="bgImg"></div>
            <div className="container">
                {Object.keys(formErrors).length === 0 && isSubmit ? (
                    <div className="ui message success">
                        Signed in successfully
                    </div>
                ) : (
                    console.log("Entered Details", formValues)
                )}
    
                <form onSubmit={handleSubmit}>
                    <h1>Sign Up</h1>
                    <div className="ui divider"></div>
                    <div className="ui form">
                        <div className="field">
                            <label>Username</label>
                            <input
                                type="text"
                                name="username"
                                placeholder="Choose a username"
                                value={formValues.username}
                                onChange={handleChange}
                            />
                        </div>
                        <p>{formErrors.username}</p>
                        <div className="field">
                            <label>Email</label>
                            <input
                                type="text"
                                name="email"
                                placeholder="Email"
                                value={formValues.email}
                                onChange={handleChange}
                            />
                        </div>
                        <p>{formErrors.email}</p>
                        <div className="field">
                            <label>Phone Number</label>
                            <input
                                type="text"
                                name="phone_number"
                                placeholder="Phone Number"
                                value={formValues.phone_number}
                                onChange={handleChange}
                            />
                        </div>
                        <p>{formErrors.phone_number}</p>
                        <div className="field">
                            <label>Password</label>
                            <input
                                type="password"
                                name="password"
                                placeholder="Password"
                                value={formValues.password}
                                onChange={handleChange}
                            />
                        </div>
                        <p>{formErrors.password}</p>
                        <div className="field">
                            <label>Confirm Password</label>
                            <input
                                type="password"
                                name="confirmPassword"
                                placeholder="Confirm password"
                                value={formValues.confirmPassword}
                                onChange={handleChange}
                            />
                        </div>
                        <p>{formErrors.confirmPassword}</p>
                        <button className="fluid ui button blue">Submit</button>
                    </div>
                </form>
                <div className="text">
                    Already have an account? <span><a href='#'>Login</a></span>
                </div>
            </div>{" "}
        </>
    );
}

export default Signup;