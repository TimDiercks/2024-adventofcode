package utils

import "slices"

type CheatPath struct {
	Position     Position
	Visited      []Position
	CheatedSteps int
}

type Position struct {
	X, Y int
}

type Cheat struct {
	Start Position
	End   Position
	Steps int
}

func (position Position) Add(other Position) Position {
	position.X += other.X
	position.Y += other.Y
	return position
}

func (path *CheatPath) GetPossibleMoves(track *RaceTrack, paths *[]CheatPath, maxCheatSteps int) {
	path.Visited = append(path.Visited, path.Position)
	for _, direction := range DIRECTIONS {
		newPosition := path.Position.Add(direction)
		if slices.Contains(path.Visited, newPosition) {
			continue
		}
		if !track.InsideBounds(newPosition) {
			continue
		}
		isWall := track.IsWall(newPosition)
		newCheatSteps := path.CheatedSteps + 1
		if isWall && newCheatSteps >= maxCheatSteps {
			continue
		}

		*paths = append(*paths, CheatPath{
			Position:     newPosition,
			Visited:      slices.Clone(path.Visited),
			CheatedSteps: newCheatSteps,
		})
	}
}
