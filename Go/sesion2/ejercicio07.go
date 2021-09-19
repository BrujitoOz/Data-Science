package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"time"
)

var wg sync.WaitGroup

func cargar(vec *[50000]int, aleatorio *rand.Rand) {
	for f := 0; f < len(vec); f++ {
		vec[f] = aleatorio.Intn(100)
	}
}

func ordenar(vec *[50000]int) {
	for k := 1; k < len(vec); k++ {
		for f := 0; f < len(vec)-k; f++ {
			if vec[f] > vec[f+1] {
				aux := vec[f]
				vec[f] = vec[f+1]
				vec[f+1] = aux
			}
		}
	}
	wg.Done()
}

func diferenciaTiempo(hora1, hora2 time.Time) time.Duration {
	diferencia := hora2.Sub(hora1)
	return diferencia
}

func main() {
	runtime.GOMAXPROCS(1)
	aleatorio := rand.New(rand.NewSource(time.Now().UnixNano()))
	var vec1 [50000]int
	var vec2 [50000]int
	cargar(&vec1, aleatorio)
	cargar(&vec2, aleatorio)

	var hora1, hora2 time.Time
	hora1 = time.Now()
	wg.Add(2)
	go ordenar(&vec1)
	go ordenar(&vec2)
	wg.Wait()
	hora2 = time.Now()
	di := diferenciaTiempo(hora1, hora2)
	fmt.Println("Cantidad de segundos de diferencia:", di.Seconds())
}
