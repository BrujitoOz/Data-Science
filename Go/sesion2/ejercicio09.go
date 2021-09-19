package main

import (
	"fmt"
	"sync"
)

var n int = 1
var wg sync.WaitGroup

func p() {
	for n < 1 { // p1

		n = n + 1 // p2
	}
	wg.Done()
}
func q() {
	for n >= 0 { // q1

		n = n - 1 // q2
	}
	wg.Done()

}
func main() {
	wg.Add(2)
	go p()
	go q()
	wg.Wait()
	fmt.Println(n)

}
