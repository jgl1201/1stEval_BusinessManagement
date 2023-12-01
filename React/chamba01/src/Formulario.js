import React, { useState } from 'react';

function Formulario() {
    const [name, setName] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        alert('Un nombre fue enviado: ' + name);
    }

    const handleChange = (event) => {
        setName(event.target.value);
    }

    return (
        <form onSubmit={handleSubmit}>
        <label>
            Nombre:
            <input type="text" value={name} onChange={handleChange} />
        </label>
        <button type="submit">Enviar</button>
        </form>
    );
}

export default Formulario;