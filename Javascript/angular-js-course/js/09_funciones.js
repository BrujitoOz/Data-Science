"use strict"

function listado(fruta1, fruta2, ...lol) {
    console.log(fruta1, fruta2)
    console.log(lol)

}
listado("sos", "sas", "asd","gfdg","sf");
var frutas = ["naranja", "pera"]
listado(...frutas, "sandia")