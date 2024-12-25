package utils

import (
	"os"
	"slices"
	"strings"
)

const LOCKHEIGHT = 7

func GetInput(fileName string) ([][]int, [][]int, error) {
	buf, err := os.ReadFile(fileName)
	if err != nil {
		return nil, nil, err
	}
	data := string(buf)
	blocks := strings.Split(data, "\n\n")

	keys := make([][]int, 0)
	locks := make([][]int, 0)

	heights := make([]int, 5)
	for _, block := range blocks {
		blockRows := strings.Split(block, "\n")
		isLock := false
		if blockRows[0] == "#####" {
			isLock = true
		}
		for column := 0; column < len(blockRows[0]); column++ {
			heights[column] = 0
			for row := 1; row < LOCKHEIGHT-1; row++ {
				if blockRows[row][column] == '#' {
					heights[column] += 1
				}
			}
		}

		if isLock {
			locks = append(locks, slices.Clone(heights))
			continue
		}
		keys = append(keys, slices.Clone(heights))
	}

	return keys, locks, nil
}
