package main

import (
	"fmt"
	"time"
)

func saludar() {
	fmt.Println("Holasss")
}

func main() {
	go saludar()
	time.Sleep(time.Second)
}
