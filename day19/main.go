package main

import (
	"day19/utils"
	"fmt"
	"math"
	"slices"
	"time"
)

const TEST = false

func main() {
	inputFile := "input.txt"
	if TEST {
		inputFile = "test_input.txt"
	}

	start := time.Now()

	towelParts, designs, err := utils.GetInputData(inputFile)
	if err != nil {
		fmt.Print("Couldn't read input file")
		return
	}

	possibleDesigns := 0
	possibleDesignsCount := 0
	cache := make(map[string]int)

	for _, design := range designs {
		count := isDesignPossible(design, towelParts, cache)
		possibleDesignsCount += count
		if count > 0 {
			possibleDesigns += 1
		}
	}

	fmt.Printf("Elapsed: %v\n", time.Since(start))

	fmt.Printf("Possible designs: %d\n", possibleDesigns)
	fmt.Printf("Possible design combinations: %d\n", possibleDesignsCount)

}

func isDesignPossible(design string, towelParts []string, cache map[string]int) int {
	if design == "" {
		return 1
	}
	if cacheValue, exists := cache[design]; exists {
		return cacheValue
	}
	maxTowelLen := len(GetMaxTowel(towelParts))
	counter := 0
	for i := range int(math.Min(float64(maxTowelLen), float64(len(design)))) {
		isDesignInTowelparts := slices.Contains(towelParts, design[:i+1])
		if isDesignInTowelparts {
			counter += isDesignPossible(design[i+1:], towelParts, cache)
		}
	}
	cache[design] = counter
	return counter
}

func GetMaxTowel(towelParts []string) string {
	x := slices.MaxFunc(towelParts, func(a, b string) int {
		if len(a) > len(b) {
			return 1
		}
		return -1
	})
	return x
}
