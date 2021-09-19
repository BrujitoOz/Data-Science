package main

import "fmt"

func ping(c chan string) {
	for {
		c <- "ping"
	}
}
func pong(c chan string) {
	for {
		c <- "pong"
	}
}
func imprimir(c chan string) {
	for {
		fmt.Println(<-c)
	}
}
func main() {
	c := make(chan string)
	go ping(c)
	go pong(c)
	go imprimir(c)
	var input string
	fmt.Scanln(&input)
}
