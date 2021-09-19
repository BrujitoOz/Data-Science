"use strict"

var n = 444;
var t1 = "Bienvenido al curso de js curso";
var t2 = "es muy buen curso";
var busqueda = t1.match("curso")
console.log(busqueda)
busqueda = t1.match(/curso/g)
console.log(busqueda)
busqueda = t1.search("curso")
console.log(busqueda)
busqueda = t1.indexOf("curso")
console.log(busqueda)
busqueda = t1.lastIndexOf("curso")
console.log(busqueda)
busqueda = t1.substr(12,5)
console.log(busqueda)
busqueda = t1.charAt(12)
console.log(busqueda)
busqueda = t1.startsWith("Bien")
console.log(busqueda)
busqueda = t1.endsWith("curso")
console.log(busqueda)
busqueda = t1.includes("cur")
console.log(busqueda)
console.log(t1.length)

var lol = t1.replace("curso", "sas")
console.log(lol)
lol = t1.slice(14)
console.log(lol)
console.log(lol.split(" "))

var t3 = " asdad   "
console.log(t3.trim())
