package main

import (
	"day19/utils"
	"fmt"
	"strings"
)

const TEST = false

func main() {
	inputFile := "input.txt"
	if TEST {
		inputFile = "test_input.txt"
	}

	towelParts, designs, err := utils.GetInputData(inputFile)
	if err != nil {
		fmt.Print("Couldn't read input file")
		return
	}
	_ = towelParts

	possibleDesigns := 0

	for _, design := range designs {
		isPossible := isDesignPossible(design, &towelParts)
		if isPossible {
			possibleDesigns++
		}
	}

	fmt.Printf("Possible designs: %d\n", possibleDesigns)

}

func isDesignPossible(design string, towelParts *[]string) bool {
	// Total list of towels to be computed
	partialTowels := make([]string, 0, 2*len(*towelParts))
	checkedStrings := make(map[string]bool)

	found := false
	partialTowel := ""
	newPartialTowel := ""
	for {
		if len(partialTowels) > 0 {
			partialTowel = partialTowels[len(partialTowels)-1]
			partialTowels = partialTowels[:len(partialTowels)-1]
		}

		for _, towelPart := range *towelParts {
			newPartialTowel = partialTowel + towelPart
			if checkedStrings[newPartialTowel] {
				continue
			}
			checkedStrings[newPartialTowel] = true
			if len(partialTowel) > len(design) {
				continue
			}
			if strings.HasPrefix(design, newPartialTowel) {
				if design == newPartialTowel {
					found = true
					break
				}
				partialTowels = append(partialTowels, newPartialTowel)
			}
		}

		if len(partialTowels) == 0 || found {
			break
		}

	}
	return found
}
