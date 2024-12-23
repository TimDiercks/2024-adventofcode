package main

import (
	"day22/utils"
	"fmt"
	"strconv"
	"strings"
	"sync"
)

const TEST = false

func sliceToString(slice []int) string {
	return fmt.Sprint(slice)
}

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

	secretsList := make([][]int, len(secrets))
	secretsBuy := make([][]int, len(secrets))

	permutations := make(map[string]struct{})
	patternValues := make([]map[string]int, 0)
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
				pattern := sliceToString(currentPattern)
				_, exists := (patternValues[j])[pattern]
				if exists {
					continue
				}
				permutations[pattern] = struct{}{}
				patternValues[j][pattern] = secretStep
			}
		}
	}

	maxPattern := ""
	maxBananas := 0

	var mutex sync.Mutex
	var wg sync.WaitGroup

	for permutation := range permutations {
		wg.Add(1)
		go func(permutation string) {
			defer wg.Done()
			currentBananas := 0

			for _, secret := range patternValues {
				value, exists := secret[permutation]
				if !exists {
					continue
				}
				currentBananas += value
			}

			mutex.Lock()
			if currentBananas > maxBananas {
				maxPattern = permutation
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
