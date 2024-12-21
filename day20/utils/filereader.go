package utils

import (
	"os"
	"strings"
)

func GetRaceTrack(fileName string) (*RaceTrack, error) {
	buf, err := os.ReadFile(fileName)
	if err != nil {
		return nil, err
	}
	data := string(buf)
	rows := strings.Split(data, "\n")
	raceTrack := RaceTrack{
		track:  make([][]string, 0, len(rows)),
		width:  len(rows[0]),
		height: len(rows),
	}
	for _, row := range rows {
		raceTrack.track = append(raceTrack.track, strings.Split(row, ""))
	}

	return &raceTrack, nil
}
