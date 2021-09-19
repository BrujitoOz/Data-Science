package main

import "fmt"

func saludar(p int) {
	fmt.Println("Hola proceso", p)
}
func pausa() {
	var input string
	fmt.Scanln(&input)
}
func main() {
	for i := 0; i < 5; i++ {
		go saludar(i + 1)
	}
	fmt.Println("Procesando...")
	pausa()
}
