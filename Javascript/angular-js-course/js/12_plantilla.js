"use strict"

var nombre = prompt("Nombre:");
var apellidos = prompt("Apellidos:")

var texto = `
    <h1>hola que tal</h1>
    <h3>Mi nombre es: ${nombre}</h3>
    <h3>Mis apellidos son: ${apellidos}</h3>
`;
document.write(texto)