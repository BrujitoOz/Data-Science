package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Print("Ingrese un numero: ")
	bufferIn := bufio.NewReader(os.Stdin)
	dato, _ := bufferIn.ReadString('\n')
	dato = strings.TrimRight(dato, "\r\n")
	num, _ := strconv.Atoi(dato)
	evaluar(num)

}
func evaluar(num int) {
	if num%2 == 0 {
		fmt.Println("El numero", num, "es divisor de 2")
	} else if num%3 == 0 {
		fmt.Println("El numero", num, "es divisor de 3")
	}
}
