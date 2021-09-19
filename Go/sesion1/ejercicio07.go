package main

import "fmt"

func main() {
	arreglo := [7]int{5, 3, 2, 7, 8, 9, 1}
	for i, v := range arreglo {
		fmt.Printf("El valor de v es %d en la posicion #%d\n", v, i)
	}
	i := 0
	for {
		fmt.Println(i)
		if i == 4 {
			break
		}
		i++
	}
	for i := 1; i <= 10; i++ {
		println("lol")
	}
}
