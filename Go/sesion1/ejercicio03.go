package main

import "fmt"

func main() {
	fmt.Print("Ingrese un numero flotante: ")
	var num float64
	fmt.Scanf("%f", &num)

	doble := num * 2
	fmt.Println("El doble de", num, " es:", doble)
}
