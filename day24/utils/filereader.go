package utils

import (
	"os"
	"strings"
)

type Gate struct {
	InputA    string
	InputB    string
	Operation string
	Output    string
}

func GetInput(fileName string) (map[string]bool, map[string]Gate, error) {
	buf, err := os.ReadFile(fileName)
	if err != nil {
		return nil, nil, err
	}
	data := string(buf)
	blocks := strings.Split(data, "\n\n")
	variableRows := strings.Split(blocks[0], "\n")
	formulaRows := strings.Split(blocks[1], "\n")
	variables := make(map[string]bool)
	formulas := make(map[string]Gate)
	for _, row := range variableRows {
		rowSplit := strings.Split(row, ": ")
		variables[rowSplit[0]] = rowSplit[1] == "1"
	}
	for _, row := range formulaRows {
		rowSplit := strings.Split(row, " -> ")
		output := rowSplit[1]
		inputSplit := strings.Split(rowSplit[0], " ")
		inputA := inputSplit[0]
		operation := inputSplit[1]
		inputB := inputSplit[2]
		formulas[rowSplit[1]] = Gate{
			InputA:    inputA,
			InputB:    inputB,
			Operation: operation,
			Output:    output,
		}
	}

	return variables, formulas, nil
}
