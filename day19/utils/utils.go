package utils

import (
	"os"
	"strings"
)

func GetInputData(fileName string) ([]string, []string, error) {
	buf, err := os.ReadFile(fileName)
	if err != nil {
		return nil, nil, err
	}
	data := string(buf)
	dataSplit := strings.Split(data, "\n\n")
	towelParts := strings.Split(dataSplit[0], ", ")
	designs := strings.Split(dataSplit[1], "\n")

	return towelParts, designs, nil
}

func DeleteAtIndex[T any](slice []T, index int) []T {
	return append(slice[:index], slice[index+1:]...)
}
