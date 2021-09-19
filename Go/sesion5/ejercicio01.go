package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	m := new(sync.Mutex)
	for i := 0; i < 10; i++ {
		func(i int) {
			m.Lock() // Bloquear el acceso de algún otro proceso al actual
			fmt.Println(i, "SC Line1")
			time.Sleep(time.Second)
			fmt.Println(i, "SC Line2")
			m.Unlock() // Desbloqueamos dando la posibilidad de otro proceso ingrese a la SC
		}(i)
	}
	// pausa
	var input string
	fmt.Scanln(&input)

}
