package main

import "fmt"

var turno int = 1

func p() {
	for {
		fmt.Println("Line01 SNC P")
		fmt.Println("Line02 SNC P")
		// condicion Preprotocol
		for turno != 1 {
			// espera
		}
		// Sección Critica
		fmt.Println("Line01 SC P")
		fmt.Println("Line02 SC P")
		// Postprotocol
		turno = 2
	}
}
func q() {
	for {
		fmt.Println("Line01 SNC Q")
		fmt.Println("Line02 SNC Q")
		// condicion Preprotocol
		for turno != 2 {
			// espera
		}
		// Sección Critica
		fmt.Println("Line01 SC Q")
		fmt.Println("Line02 SC Q")
		// Postprotocol
		turno = 1
	}
}
func main() {
	go p()
	q()
}
