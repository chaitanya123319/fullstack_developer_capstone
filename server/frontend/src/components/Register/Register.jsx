
import React, { useState } from 'react';

function Register() {
    const [formData, setFormData] = useState({
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        password: ''
    });

    const [message, setMessage] = useState('');
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('');
        setLoading(true);

        try {
            const response = await fetch(
                'http://127.0.0.1:8000/api/register/',
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error || 'Registration failed'
                );
            }

            setMessage('Registration successful!');

            setFormData({
                username: '',
                first_name: '',
                last_name: '',
                email: '',
                password: ''
            });

        } catch (error) {
            setMessage(error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={styles.container}>
            <form onSubmit={handleSubmit} style={styles.form}>

                <h1 style={styles.heading}>
                    Cars Dealership
                </h1>

                <h2 style={styles.subheading}>
                    Create Your Account
                </h2>

                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={formData.username}
                    onChange={handleChange}
                    autoComplete="username"
                    required
                />

                <input
                    type="text"
                    name="first_name"
                    placeholder="First Name"
                    value={formData.first_name}
                    onChange={handleChange}
                    autoComplete="given-name"
                    required
                />

                <input
                    type="text"
                    name="last_name"
                    placeholder="Last Name"
                    value={formData.last_name}
                    onChange={handleChange}
                    autoComplete="family-name"
                    required
                />

                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={handleChange}
                    autoComplete="email"
                    required
                />

                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                    autoComplete="new-password"
                    required
                />

                <button
                    type="submit"
                    disabled={loading}
                    style={styles.button}
                >
                    {loading ? 'Registering...' : 'Register'}
                </button>

                {message && (
                    <p style={styles.message}>
                        {message}
                    </p>
                )}

            </form>
        </div>
    );
}

const styles = {
    container: {
        minHeight: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#f1f5f9',
        padding: '20px'
    },

    form: {
        backgroundColor: '#ffffff',
        padding: '40px',
        borderRadius: '15px',
        width: '100%',
        maxWidth: '450px',
        display: 'flex',
        flexDirection: 'column',
        gap: '18px',
        boxShadow: '0 8px 30px rgba(0,0,0,0.10)'
    },

    heading: {
        color: '#1e293b',
        textAlign: 'center',
        fontSize: '30px',
        marginBottom: '5px'
    },

    subheading: {
        color: '#475569',
        textAlign: 'center',
        fontSize: '20px',
        marginBottom: '12px'
    },

    button: {
        padding: '13px',
        backgroundColor: '#2563eb',
        color: '#ffffff',
        border: 'none',
        borderRadius: '6px',
        fontSize: '16px',
        fontWeight: 'bold',
        cursor: 'pointer'
    },

    message: {
        textAlign: 'center',
        color: '#15803d',
        fontWeight: 'bold'
    }
};

export default Register;
