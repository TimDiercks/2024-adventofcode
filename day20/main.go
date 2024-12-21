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
		for x := -maxCheatSteps; x <= maxCheatSteps; x++ {
			remainingSteps := maxCheatSteps - int(math.Abs(float64(x)))
			for y := -remainingSteps; y <= remainingSteps; y++ {
				doneSteps := int(math.Abs(float64(x)) + math.Abs(float64(y)))
				newPosition := utils.Position{
					X: position.X + x,
					Y: position.Y + y,
				}
				newSteps, exists := stepsTilFinish[newPosition]
				if !exists {
					continue
				}
				savedSteps := steps - newSteps - doneSteps
				if savedSteps >= threshold {
					amountCheats += 1
				}
			}
		}
	}

	fmt.Printf("Amount of cheats: %d\n", amountCheats)

}
