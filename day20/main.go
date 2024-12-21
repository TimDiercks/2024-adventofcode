package main

import (
	"day20/utils"
	"fmt"
	"math"
)

const TEST = false
const PART = 2

func main() {
	inputFile := "input.txt"
	if TEST {
		inputFile = "test_input.txt"
	}
	maxCheatSteps := 2
	if PART == 2 {
		maxCheatSteps = 20
	}

	raceTrack, err := utils.GetRaceTrack(inputFile)
	if err != nil {
		fmt.Print("Couldn't read input file")
		return
	}
	stepsTilFinish := utils.GetOriginalPathStepLength(raceTrack)

	threshold := 100
	amountCheats := 0
	for position, steps := range stepsTilFinish {
		for secondPosition, secondSteps := range stepsTilFinish {
			diffX := position.X - secondPosition.X
			diffY := position.Y - secondPosition.Y
			doneSteps := int(math.Abs(float64(diffX)) + math.Abs(float64(diffY)))
			if doneSteps > maxCheatSteps {
				continue
			}
			savedSteps := steps - secondSteps - doneSteps
			if savedSteps >= threshold {
				amountCheats += 1
			}
		}
	}

	fmt.Printf("Amount of cheats: %d\n", amountCheats)

}
