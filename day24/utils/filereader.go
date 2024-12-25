package utils

import (
	"os"
	"strings"
)

func GetInput(fileName string) (map[string]bool, map[string][]string, error) {
	buf, err := os.ReadFile(fileName)
	if err != nil {
		return nil, nil, err
	}
	data := string(buf)
	blocks := strings.Split(data, "\n\n")
	variableRows := strings.Split(blocks[0], "\n")
	formulaRows := strings.Split(blocks[1], "\n")
	variables := make(map[string]bool)
	formulas := make(map[string][]string)
	for _, row := range variableRows {
		rowSplit := strings.Split(row, ": ")
		variables[rowSplit[0]] = rowSplit[1] == "1"
	}
	for _, row := range formulaRows {
		rowSplit := strings.Split(row, " -> ")
		formulas[rowSplit[1]] = strings.Split(rowSplit[0], " ")
	}

	return variables, formulas, nil
}
