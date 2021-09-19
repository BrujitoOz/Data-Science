// Document object model: elementos de la pagina web, como las etiquetas
function cambiacolor(color){
    caja.style.color = color
}


// var caja = document.getElementById("micaja")
var caja = document.querySelector("#micaja")
caja.innerHTML = "Texto en la caja"
caja.style.padding = "20px"
caja.style.background = "green"
caja.className = "hola"
console.log(caja)

var todosLosDivs = document.getElementsByTagName("div")
var contenidoEnTexto = todosLosDivs[2]
contenidoEnTexto.innerHTML = "lol"
contenidoEnTexto.style.background = "red"
console.log(contenidoEnTexto)

