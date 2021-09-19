package main

import "fmt"

func envio(c chan int) {
	// envio
	c <- 5
}

func main() {
	c := make(chan int) // sincrona
	go envio(c)
	fmt.Println(<-c) // leo lo que llega a traves del canal
}
