package main

import (
	"day20/utils"
	"fmt"
)

const TEST = false
const PART = 1

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
		startPath := utils.CheatPath{
			Position:     position,
			CheatedSteps: 0,
		}
		visited := make(map[utils.Position]bool)
		paths := make([]utils.CheatPath, 0)
		startPath.GetPossibleMoves(raceTrack, &paths, maxCheatSteps, &visited)
		endings := make(map[utils.Position]bool)

		for len(paths) != 0 {
			currentPath := paths[0]
			paths = paths[1:]
			stepsFromNewPos, exists := stepsTilFinish[currentPath.Position]
			if exists {
				if endings[currentPath.Position] {
					continue
				}
				endings[currentPath.Position] = true
				savedSteps := steps - stepsFromNewPos - currentPath.CheatedSteps
				if savedSteps >= threshold {
					amountCheats += 1
				}
				continue
			}
			currentPath.GetPossibleMoves(raceTrack, &paths, maxCheatSteps, &visited)
		}

	}

	fmt.Printf("Amount of cheats: %d\n", amountCheats)

}
