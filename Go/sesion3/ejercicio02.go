package main

import "fmt"

var wantp bool = false
var wantq bool = false

func p() {
	for {
		fmt.Println("Line01 SNC P")
		fmt.Println("Line02 SNC P")
		for wantq {
			// espera
		}
		wantp = true
		fmt.Println("Line01 SC P")
		fmt.Println("Line02 SC P")
		wantp = false
	}
}
func q() {
	for {
		fmt.Println("Line01 SNC Q")
		fmt.Println("Line02 SNC Q")
		for wantp {
			// espera
		}
		wantq = true
		fmt.Println("Line01 SC Q")
		fmt.Println("Line02 SC Q")
		wantq = false
	}
}

func main() {
	go p()
	q()
}
