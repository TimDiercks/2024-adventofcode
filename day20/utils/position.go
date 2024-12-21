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
