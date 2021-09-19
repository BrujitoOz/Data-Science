package main

import "fmt"

func sumar(arr []int, c chan int) {
	suma := 0
	for _, v := range arr {
		suma += v
	}
	c <- suma

}
func main() {
	arreglo := []int{6, 2, 8, 9, 4, 1}
	c := make(chan int)
	go sumar(arreglo[:len(arreglo)/2], c)
	go sumar(arreglo[len(arreglo)/2:], c)
	a, b := <-c, <-c
	fmt.Println(a)
	fmt.Println(b)
	fmt.Print("la suma es:", a+b)
}
