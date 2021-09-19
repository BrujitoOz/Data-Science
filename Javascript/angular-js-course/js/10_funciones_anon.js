"use strict"

function suname(n1, n2, sumYmuestra, sumXdos) {
    var sumar = n1 + n2;
    sumYmuestra(sumar);

    return sumar;
}
suname(5,7, dato => {console.log("la suma es: " + dato)}, dato => {console.log("la suma por dos es ",+(dato*2) );});
