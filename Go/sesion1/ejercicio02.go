package main

import "fmt"

const igv float64 = 18.0

func main() {
	var x string = "Hola a todos"
	fmt.Println(x)

	dato := 20
	fmt.Println("Valor de la variable dato es: ", dato)

	var (
		nombre string
		edad   int
	)
	nombre = "Juan"
	edad = 25
	fmt.Println("El nombre es", nombre, ",su edad es", edad)
}
