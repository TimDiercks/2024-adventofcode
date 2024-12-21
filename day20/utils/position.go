package utils

type CheatPath struct {
	Position     Position
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

func (path *CheatPath) GetPossibleMoves(track *RaceTrack, paths *[]CheatPath, maxCheatSteps int, visited *map[Position]bool) {
	(*visited)[path.Position] = true
	for _, direction := range DIRECTIONS {
		newPosition := path.Position.Add(direction)
		if (*visited)[newPosition] {
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
			CheatedSteps: newCheatSteps,
		})
	}
}
