package main

import (
	"fmt"
	"time"
)

func proceso3(c3 chan string) {
	for {
		c3 <- "Datos enviados desde el proceso 3"
		time.Sleep(time.Second * 4)
	}
}

func main() {
	// crear canales sincronos
	c1 := make(chan string)
	c2 := make(chan string)
	c3 := make(chan string)
	// funciones
	go func() {
		for {
			c1 <- "Datos enviados desde el proceso 1"
			time.Sleep(time.Second * 3)
		}
	}()
	go func() {
		for {
			c2 <- "Datos enviados desde el proceso 2"
			time.Sleep(time.Second * 2)
		}
	}()
	go proceso3(c3)
	// interceptar
	go func() {
		for {
			select {
			case msg1 := <-c1:
				fmt.Println(msg1)
			case msg2 := <-c2:
				fmt.Println(msg2)
			case <-c3:
				fmt.Println("Mensaje 3")
			case <-time.After(time.Second):
				fmt.Println("Tiempo de espera caducado")

			}
		}
	}()
	var input string
	fmt.Scanln(&input)
}
