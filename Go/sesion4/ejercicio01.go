package main

import "fmt"

func p(c chan int) {
	c <- 5
}

func main() {
	c := make(chan int)
	go p(c)
	go p(c)
	n := <-c
	g := <-c
	f := <-c
	fmt.Println(n, g, f)
}
