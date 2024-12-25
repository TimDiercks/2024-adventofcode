package main

import (
	"day24/utils"
	"fmt"
	"strconv"
	"strings"
	"time"
)

const TEST = false

func main() {
	inputFile := "input.txt"
	if TEST {
		inputFile = "test_input.txt"
	}
	start := time.Now()
	variables, formulas, err := utils.GetInput(inputFile)
	if err != nil {
		return
	}

	for len(formulas) != 0 {
		for key, formula := range formulas {
			firstOperand := formula[0]
			a, exists := variables[firstOperand]
			if !exists {
				continue
			}
			secondOperand := formula[2]
			b, exists := variables[secondOperand]
			if !exists {
				continue
			}

			variables[key] = computeFormula(formula[1], a, b)

			delete(formulas, key)
		}
	}

	result := int64(0)
	for key, variable := range variables {
		if !strings.HasPrefix(key, "z") {
			continue
		}
		if !variable {
			continue
		}
		indexStr := strings.ReplaceAll(key, "z", "")
		index, err := strconv.Atoi(indexStr)
		if err != nil {
			panic("parsing error")
		}
		result += 1 << index
	}
	fmt.Printf("result: %d\n", result)
	fmt.Println(time.Since(start))
}

func computeFormula(operation string, a, b bool) bool {
	switch operation {
	case "AND":
		return AND(a, b)
	case "OR":
		return OR(a, b)
	case "XOR":
		return XOR(a, b)
	}
	panic("Switch case should be exhaustive")
}

func AND(a, b bool) bool {
	return a && b
}

func OR(a, b bool) bool {
	return a || b
}

func XOR(a, b bool) bool {
	return a != b
}
