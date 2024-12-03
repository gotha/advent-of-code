package main

import (
	"fmt"
	"os"
	"slices"
	"sort"
	"strconv"
	"strings"
)

const (
	HandTypeFive = iota + 1
	HandTypeFour
	HandTypeFullHouse
	HandTypeThree
	HandTypeTwoPair
	HandTypePair
	HandTypeHigh
)

// first part order
//var cards = map[string]int{
//	"A": 1,
//	"K": 2,
//	"Q": 3,
//	"J": 4,
//	"T": 5,
//	"9": 6,
//	"8": 7,
//	"7": 8,
//	"6": 9,
//	"5": 10,
//	"4": 11,
//	"3": 12,
//	"2": 13,
//}

var cards = map[string]int{
	"A": 1,
	"K": 2,
	"Q": 3,
	"T": 4,
	"9": 5,
	"8": 6,
	"7": 7,
	"6": 8,
	"5": 9,
	"4": 10,
	"3": 11,
	"2": 12,
	"J": 13,
}

func typeToString(i int) string {
	switch i {
	case 1:
		return "five_of_a kind"
	case 2:
		return "four of a kind"
	case 3:
		return "full house"
	case 4:
		return "three of a kind"
	case 5:
		return "two pair"
	case 6:
		return "pair"
	case 7:
		return "high"
	}
	return "maikamudaiba"
}

func getType(cards []string) int {
	data := map[string]int{}
	for _, c := range cards {
		data[c] += 1
	}

	num_twos := 0
	max_value := 0
	for _, v := range data {
		if v > max_value {
			max_value = v
		}
		if v == 2 {
			num_twos += 1
		}
	}
	if max_value == 1 {
		return HandTypeHigh
	}
	if max_value == 2 {
		if num_twos > 1 {
			return HandTypeTwoPair
		}
		return HandTypePair
	}
	if max_value == 3 {
		if len(data) == 2 {
			return HandTypeFullHouse
		}
		if len(data) == 3 {
			return HandTypeThree
		}
	}
	if max_value == 4 {
		return HandTypeFour
	}
	if max_value == 5 {
		return HandTypeFive
	}

	panic(fmt.Sprintf("unknown hand type: %+v", cards))
}

type Hand struct {
	hand         string
	origCards    []string
	optimalCards []string
	bid          int
}

func NewHand(hand string, bid int) Hand {
	cards := strings.Split(hand, "")
	return Hand{
		hand:      hand,
		origCards: cards,
		bid:       bid,
	}
}

func (h *Hand) CalcBestVersion() string {
	if !slices.Contains(h.origCards, "J") {
		return h.hand
	}

	data := map[string]int{}
	for _, c := range h.origCards {
		if c != "J" {
			data[c] += 1
		}
	}

	max_value := 0
	for _, v := range data {
		if v > max_value {
			max_value = v
		}
	}

	// seems like we have all Js
	if max_value == 0 {
		return "AAAAA"
	}

	// lets determine which group we want to join
	max_cards := []string{}
	for k, v := range data {
		if v == max_value {
			max_cards = append(max_cards, k)
		}
	}

	card_to_join := max_cards[0]
	if len(max_cards) > 1 {
		for _, v := range max_cards {
			v1 := cards[card_to_join]
			v2 := cards[v]
			if v2 < v1 {
				card_to_join = v
			}
		}
	}

	newHand := ""
	for _, c := range h.origCards {
		if c == "J" {
			newHand += card_to_join
			continue
		}
		newHand += c
	}

	return newHand
}

func (h *Hand) CmpBestVersion(other Hand) bool {
	bestVersion := h.CalcBestVersion()
	otherBest := other.CalcBestVersion()
	bestVersionArr := strings.Split(bestVersion, "")
	otherBestArr := strings.Split(otherBest, "")

	t1 := getType(bestVersionArr)
	t2 := getType(otherBestArr)
	if t1 != t2 {
		return t1 > t2
	}

	num_cards := len(h.hand)
	// if both are the same type - compare original string order
	for i := 0; i < num_cards; i++ {
		c1 := h.origCards[i]
		c2 := other.origCards[i]
		v1 := cards[c1]
		v2 := cards[c2]
		if v1 == v2 {
			continue
		}
		return v1 > v2
	}
	return true
}

func (h *Hand) Cmp(other Hand) bool {
	t1 := getType(h.origCards)
	t2 := getType(other.origCards)
	if t1 != t2 {
		return t1 > t2
	}

	num_cards := len(h.hand)
	for i := 0; i < num_cards; i++ {
		c1 := h.origCards[i]
		c2 := other.origCards[i]
		v1 := cards[c1]
		v2 := cards[c2]
		if v1 == v2 {
			continue
		}
		return v1 > v2
	}
	return true
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
	file_data := string(buf)
	lines := strings.Split(file_data, "\n")
	lines = lines[0 : len(lines)-1]

	hands := []Hand{}
	for _, l := range lines {
		parts := strings.Split(l, " ")
		bid, _ := strconv.Atoi(parts[1])
		hand := NewHand(parts[0], bid)
		hands = append(hands, hand)
	}

	sort.Slice(hands, func(j, k int) bool {
		// return hands[j].Cmp(hands[k])
		return hands[j].CmpBestVersion(hands[k])
	})

	sum := 0
	for r, h := range hands {
		rank := r + 1
		best := h.CalcBestVersion()
		bestArr := strings.Split(best, "")
		bestType := typeToString(getType(bestArr))
		fmt.Printf("hand: %s; bestV: %s, type: %s; rank: %d; bid: %d;\n", h.hand, best, bestType, rank, h.bid)
		sum += rank * h.bid
	}
	fmt.Printf("%+v\n", sum)
}
