package main

import (
	"day24/utils"
	"fmt"
	"time"
)

const TEST = false

func main() {
	inputFile := "input.txt"
	if TEST {
		inputFile = "test_input.txt"
	}
	start := time.Now()
	keys, locks, err := utils.GetInput(inputFile)
	if err != nil {
		return
	}

	nonOverlapping := 0

	for _, lock := range locks {
		for _, key := range keys {
			nonOverlapping += checkOverlap(lock, key)
		}
	}

	fmt.Println("NonOverlapping: ", nonOverlapping)
	fmt.Println(time.Since(start))
}

func checkOverlap(lock []int, key []int) int {
	for i, lockHeight := range lock {
		if lockHeight+key[i] > utils.LOCKHEIGHT-2 {
			return 0
		}
	}
	return 1
}
