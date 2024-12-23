package utils

import (
	"os"
	"strconv"
	"strings"
)

func GetInput(fileName string) ([]int, error) {
	buf, err := os.ReadFile(fileName)
	if err != nil {
		return nil, err
	}
	data := string(buf)
	rows := strings.Split(data, "\n")
	result := []int{}
	for _, row := range rows {
		number, err := strconv.Atoi(row)
		if err != nil {
			return nil, err
		}
		result = append(result, number)
	}

	return result, nil
}
