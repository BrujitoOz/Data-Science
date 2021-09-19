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
	ingreso, er := bufferIn.ReadString('\n')
	if er != nil {
		fmt.Println("error:", er.Error())
		os.Exit(1)
	}
	fmt.Print(ingreso)
	ingreso = strings.TrimRight(ingreso, "\r\n")
	num, err := strconv.Atoi(ingreso)
	if err != nil {
		fmt.Println("Error: ", err.Error())
		os.Exit(1)
	}
	doble := num * 2
	fmt.Println("el doble de", num, " es ", doble)
}
