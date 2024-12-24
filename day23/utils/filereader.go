package utils

import (
	"os"
	"strings"
)

func GetInput(fileName string) ([][]string, error) {
	buf, err := os.ReadFile(fileName)
	if err != nil {
		return nil, err
	}
	data := string(buf)
	rows := strings.Split(data, "\n")
	result := [][]string{}
	for _, row := range rows {
		result = append(result, strings.Split(row, "-"))
	}

	return result, nil
}
