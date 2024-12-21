package utils

const WALL = "#"
const START = "S"
const END = "E"

var DIRECTIONS = [...]Position{
	{X: 1, Y: 0},
	{X: -1, Y: 0},
	{X: 0, Y: 1},
	{X: 0, Y: -1},
}

type RaceTrack struct {
	track         [][]string
	width, height int
}

func (raceTrack *RaceTrack) InsideBounds(position Position) bool {
	return position.X >= 0 && position.X < raceTrack.width && position.Y >= 0 && position.Y < raceTrack.height
}

func (raceTrack *RaceTrack) IsValue(position Position, value string) bool {
	return raceTrack.track[position.Y][position.X] == value
}

func (raceTrack *RaceTrack) IsWall(position Position) bool {
	return raceTrack.IsValue(position, WALL)
}

func (raceTrack *RaceTrack) IsFinish(position Position) bool {
	return raceTrack.IsValue(position, END)
}

func (raceTrack *RaceTrack) IsStart(position Position) bool {
	return raceTrack.IsValue(position, START)
}

func (raceTrack *RaceTrack) GetPosition(postionValue string) *Position {
	for y, row := range raceTrack.track {
		for x, entry := range row {
			if entry != postionValue {
				continue
			}
			return &Position{
				X: x,
				Y: y,
			}
		}
	}

	return nil
}

func GetOriginalPathStepLength(raceTrack *RaceTrack) map[Position]int {
	end := raceTrack.GetPosition(END)
	origPath := CheatPath{
		Position: *end,
	}
	visited := make(map[Position]bool)
	stepsTilFinish := make(map[Position]int, 0)
	stepsTaken := 0
	for {
		stepsTilFinish[origPath.Position] = stepsTaken
		if raceTrack.IsStart(origPath.Position) {
			break
		}
		visited[origPath.Position] = true

		for _, direction := range DIRECTIONS {
			newPosition := origPath.Position.Add(direction)
			if visited[newPosition] {
				continue
			}
			isWall := raceTrack.IsWall(newPosition)
			if isWall {
				continue
			}

			origPath.Position = newPosition
			break
		}

		stepsTaken++
	}
	return stepsTilFinish
}
