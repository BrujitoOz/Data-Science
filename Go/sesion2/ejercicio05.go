package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"time"
)

var wg sync.WaitGroup
var n int = 0

func pausa() {
	duracion := time.Duration(rand.Intn(251))
	time.Sleep(time.Millisecond * duracion)
}
func pq(proc string) {
	// inicia proceso p o q
	var temp int
	for i := 0; i < 10; i++ {
		temp = n
		pausa()
		n = temp + 1
		fmt.Println(proc+"2", i, temp, n)
	}
	wg.Done()
}
func main() {
	runtime.GOMAXPROCS(1)
	wg.Add(2)
	go pq("p") // proceso 1
	go pq("q") // proceso 2
	// time.Sleep(time.Second)
	wg.Wait()
	fmt.Println(n)
}
