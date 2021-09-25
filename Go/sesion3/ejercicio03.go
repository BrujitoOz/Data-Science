package main

import "fmt"

func envio(c chan int) {
	// envio
	c <- 5
}

func main() {
	c := make(chan int) // sincrona
	go envio(c)
	// mientras que no reciba nada, esta instruccion va a estar esperando
	fmt.Println(<-c) // leo lo que llega a traves del canal
}
