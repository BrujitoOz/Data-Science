
var nombres = ["Victor Robles", "Juan Lopez", "Manolo Garcia", "Jose Martin", 52, true]
var lenguajes = new Array("PHP", "JS", "GO")
//var elemento = parseInt(prompt("Que elemento del array quieres?", 0))
console.log(nombres)
console.log(lenguajes)
console.log(nombres.length)
//alert(nombres[elemento])

document.write("<h1>Lenguajes de programacion</h1>")
document.write("<ul>")
for(const e of lenguajes) {
    document.write("<li>" +  e + "</li>")
}
document.write("</ul>")

var peliculas = ["La verdad duele", "La vida es bella", "Gran Torino"]
peliculas.sort()
document.write(peliculas)

let busqueda = lenguajes.find(function(lenguaje){
    return lenguaje == "PHP"
});
console.log(busqueda)