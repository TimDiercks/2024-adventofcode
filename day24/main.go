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
	variables, gates, err := utils.GetInput(inputFile)
	if err != nil {
		return
	}

	swapGates(gates, "rts", "z07")
	swapGates(gates, "jpj", "z12")
	swapGates(gates, "kgj", "z26")
	swapGates(gates, "chv", "vvw")

	carry := "whb"
	for i := range 44 {
		fmt.Printf("--------------%02d----------------\n", i+1)
		carry = checkGates(gates, fmt.Sprintf("x%02d", i+1), fmt.Sprintf("y%02d", i+1), carry)
	}

	for len(gates) != 0 {
		for key, gate := range gates {
			firstOperand := gate.InputA
			a, exists := variables[firstOperand]
			if !exists {
				continue
			}
			secondOperand := gate.InputB
			b, exists := variables[secondOperand]
			if !exists {
				continue
			}

			variables[key] = computeFormula(gate.Operation, a, b)

			delete(gates, key)
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

func checkGates(gates map[string]utils.Gate, inputA, inputB, carry string) string {
	xorGate := searchGate(gates, inputA, inputB, "XOR")
	andGate := searchGate(gates, inputA, inputB, "AND")
	carryXorGate := searchGate(gates, xorGate.Output, carry, "XOR")
	carryAndGate := searchGate(gates, xorGate.Output, carry, "AND")
	carryAndAndGate := searchGate(gates, carryAndGate.Output, andGate.Output, "OR")
	_, _ = xorGate, andGate
	_ = carryXorGate
	_ = carryAndGate
	return carryAndAndGate.Output
}

func searchGate(gates map[string]utils.Gate, inputA, inputB, operation string) utils.Gate {
	for _, gate := range gates {
		if gate.Operation != operation {
			continue
		}
		if gate.InputA != inputA && gate.InputB != inputA {
			continue
		}
		if gate.InputA != inputB && gate.InputB != inputB {
			continue
		}
		return gate
	}
	fmt.Println("NOT FOUND!", inputA, operation, inputB)
	return utils.Gate{}
}

func swapGates(gates map[string]utils.Gate, gateOutA, gateOutB string) {
	gateA, exists := gates[gateOutA]
	if !exists {
		return
	}
	gateB, exists := gates[gateOutB]
	if !exists {
		return
	}
	delete(gates, gateOutA)
	delete(gates, gateOutB)
	gates[gateOutA] = utils.Gate{
		InputA:    gateB.InputA,
		InputB:    gateB.InputB,
		Operation: gateB.Operation,
		Output:    gateA.Output,
	}
	gates[gateOutB] = utils.Gate{
		InputA:    gateA.InputA,
		InputB:    gateA.InputB,
		Operation: gateA.Operation,
		Output:    gateB.Output,
	}
}

// func checkgates()

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
