package main

import (
	"fmt"
)

func main() {
	// data := [][]int{{71530, 940200}}
	data := [][]int{{47986698, 400121310111540}}

	result := 1
	for _, v := range data {
		time := v[0]
		distance := v[1]

		wins := 0
		for hold_time := 1; hold_time < distance; hold_time++ {
			move_time := time - hold_time
			if move_time <= 0 {
				break
			}
			trial_distance := hold_time * move_time
			if trial_distance > distance {
				wins += 1
			}
		}
		result = result * wins
	}
	fmt.Printf("%+v\n", result)
}
