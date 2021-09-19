package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Print("Ingrese su nombre: ")
	bufferIn := bufio.NewReader(os.Stdin)
	nombre, _ := bufferIn.ReadString('\n')
	nombre = strings.TrimRight(nombre, "\r\n")

	menu :=
		`
		**** MENU ****
		[1] Pizza
		[2] Empanada
		¿Cual es tu pedido?
	`
	println("Bienvenido", nombre)
	println(menu)
	opc, _ := bufferIn.ReadString('\n')
	opc = strings.TrimRight(opc, "\r\n")
	switch opc {
	case "1":
		fmt.Println("Usted eligio Pizza")
	case "2":
		fmt.Println("Usted eligio Empanada")
	}
	fmt.Println("Gracias por su preferencia")
}
