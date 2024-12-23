package main

import (
	"day22/utils"
	"fmt"
	"math"
	"slices"
	"strconv"
	"strings"
	"sync"
)

const TEST = false

func main() {
	inputFile := "input.txt"
	if TEST {
		inputFile = "test_input.txt"
	}

	secrets, err := utils.GetInput(inputFile)
	if err != nil {
		fmt.Print("Couldn't read input file")
		return
	}

	permutations := make([][]int, 0)
	for range 4 {
		permutations = addPermutations(permutations)
	}

	secretsList := make([][]int, len(secrets))
	secretsBuy := make([][]int, len(secrets))

	for j := range secrets {
		for range 2000 {
			secretsList[j] = append(secretsList[j], secrets[j])
			strSecret := strings.Split(fmt.Sprintf("%d", secrets[j]), "")
			buyPrice, _ := strconv.Atoi(strSecret[len(strSecret)-1])
			secretsBuy[j] = append(secretsBuy[j], buyPrice)
			evolveSecret(&secrets[j])
		}
		secretsList[j] = append(secretsList[j], secrets[j])
		strSecret := strings.Split(fmt.Sprintf("%d", secrets[j]), "")
		buyPrice, _ := strconv.Atoi(strSecret[len(strSecret)-1])
		secretsBuy[j] = append(secretsBuy[j], buyPrice)
	}

	patternValues := make([]map[string]int, 0)

	for j, secret := range secretsBuy {
		patternValues = append(patternValues, make(map[string]int))
		currentPattern := make([]int, 0, 4)
		for i, secretStep := range secret[1:] {
			diff := secretStep - secret[i]
			if len(currentPattern) >= 4 {
				currentPattern = currentPattern[1:]
			}
			currentPattern = append(currentPattern, diff)
			if len(currentPattern) == 4 {
				pattern := fmt.Sprintf("%d%d%d%d", currentPattern[0], currentPattern[1], currentPattern[2], currentPattern[3])
				_, exists := (patternValues[j])[pattern]
				if exists {
					continue
				}
				patternValues[j][pattern] = secretStep
			}
		}
	}

	maxPattern := ""
	maxBananas := 0

	var mutex sync.Mutex
	var wg sync.WaitGroup

	for _, permutation := range permutations {
		wg.Add(1)
		go func(permutation []int) {
			defer wg.Done()
			pattern := fmt.Sprintf("%d%d%d%d", permutation[0], permutation[1], permutation[2], permutation[3])
			currentBananas := 0

			for _, secret := range patternValues {
				value, exists := secret[pattern]
				if !exists {
					continue
				}
				currentBananas += value
			}

			mutex.Lock()
			if currentBananas > maxBananas {
				maxPattern = pattern
				maxBananas = currentBananas
			}
			mutex.Unlock()
		}(permutation)
	}

	wg.Wait()

	secretSum := 0

	for _, secret := range secretsList {
		secretSum += secret[2000]
	}

	fmt.Printf("Sum of secrets: %d\n", secretSum)
	fmt.Printf("MaxBananas: %d\n", maxBananas)
	fmt.Printf("MaxBananas pattern: %s\n", maxPattern)

}

func evolveSecret(secret *int) {
	result := *secret << 6
	*secret ^= result
	*secret %= 16777216
	result = *secret >> 5
	*secret ^= result
	*secret %= 16777216
	result = *secret << 11
	*secret ^= result
	*secret %= 16777216
}

func addPermutations(permutations [][]int) [][]int {
	if len(permutations) == 0 {
		permutations = append(permutations, []int{})
	}
	startLen := len(permutations[0])

	for {
		if len(permutations[0]) != startLen {
			break
		}
		permutation := permutations[0]
		permutations = permutations[1:]
		currentSum := 0
		for _, a := range permutation {
			currentSum += a
		}
		for i := -9 - int(math.Min(float64(currentSum), 0)); i < 10-int(math.Max(float64(currentSum), 0)); i++ {
			// for i := -9; i < 10; i++ {
			temp := append(permutation, i)
			permutations = append(permutations, slices.Clone(temp))
		}
	}
	return permutations
}
