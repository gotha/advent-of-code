package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type map_range struct {
	start  int
	end    int
	offset int
}

type seed_map struct {
	ranges []map_range
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("please provide input file as argument")
		os.Exit(1)
	}
	buf, err := os.ReadFile(os.Args[1])
	if err != nil {
		panic(fmt.Sprintf("Cannot read file: %s", err))
	}
	data := string(buf)
	lines := strings.Split(data, "\n")

	maps_keys := []string{"seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"}
	num_keys := len(maps_keys)

	maps := make([]seed_map, num_keys)
	for i := 0; i < num_keys; i++ {
		maps[i] = seed_map{}
	}

	seeds := []int{}

	curr_map_id := -1
outer:
	for _, l := range lines {
		if l == "" {
			continue
		}
		if strings.Index(l, "seeds:") == 0 {
			v := strings.Split(l, ": ")
			nums := strings.Split(v[1], " ")
			for _, n := range nums {
				i, _ := strconv.Atoi(n)
				seeds = append(seeds, i)
			}
			continue
		}
		for i, key := range maps_keys {
			if strings.Index(l, key) == 0 {
				curr_map_id = i
				continue outer
			}
		}

		nums := strings.Split(l, " ")
		anums := [3]int{}
		for i, s := range nums {
			v, _ := strconv.Atoi(s)
			anums[i] = v
		}
		maps[curr_map_id].ranges = append(maps[curr_map_id].ranges, map_range{
			start:  anums[1],
			end:    anums[1] + anums[2],
			offset: anums[0] - anums[1],
		})

	}

	/*
		// part 1
		min_loc := math.MaxInt64
		for _, seed := range seeds {
			fmt.Printf("%+v\n", seed)
			results := [7]int{}
			for k, m := range maps {
				seek := seed
				if k > 0 {
					seek = results[k-1]
				}
				results[k] = seek
				for _, r := range m.ranges {
					if seek >= r.start && seek < r.end {
						results[k] = seek + r.offset
						break
					}
				}
			}
			if results[6] < min_loc {
				min_loc = results[6]
			}
		}
	*/

	min_loc := math.MaxInt64
	seed_pairs := make([][]int, len(seeds)/2)
	c := 0
	for i := 0; i < len(seeds); i += 2 {
		seed_pairs[c] = append(seed_pairs[c], seeds[i])
		seed_pairs[c] = append(seed_pairs[c], seeds[i]+seeds[i+1])
		c++
	}

	for _, p := range seed_pairs {
		for seed := p[0]; seed < p[1]+1; seed += 1 {
			// fmt.Printf("%d - %d -> %d\n", p[0], p[1], seed)
			results := [7]int{}
			for k, m := range maps {
				seek := seed
				if k > 0 {
					seek = results[k-1]
				}
				results[k] = seek
				for _, r := range m.ranges {
					if seek >= r.start && seek < r.end {
						results[k] = seek + r.offset
						break
					}
				}
			}
			if results[6] < min_loc {
				min_loc = results[6]
			}

		}
	}

	fmt.Printf("%+v\n", "-------------------------")
	fmt.Printf("%+v\n", min_loc)
}
