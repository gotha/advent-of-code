package main

import (
	//"fmt"
	"testing"
)

func Test_GetType(t *testing.T) {
	tests := []struct {
		name         string
		input        []string
		expectedType int
	}{
		{"five of a kind", []string{"A", "A", "A", "A", "A"}, HandTypeFive},
		{"four of a kind", []string{"A", "A", "A", "A", "K"}, HandTypeFour},
		{"full house", []string{"A", "A", "A", "B", "B"}, HandTypeFullHouse},
		{"three of a kind", []string{"A", "A", "A", "B", "C"}, HandTypeThree},
		{"two pair", []string{"A", "A", "B", "B", "C"}, HandTypeTwoPair},
		{"pair", []string{"A", "A", "B", "C", "D"}, HandTypePair},
		{"high", []string{"A", "B", "C", "D", "E"}, HandTypeHigh},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			res := getType(tt.input)
			if res != tt.expectedType {
				t.Errorf("got: %d, exteded: %d", res, tt.expectedType)
			}
		})
	}
}

func Test_HandCompare(t *testing.T) {
	tests := []struct {
		name string
		h1   Hand
		h2   Hand
		res  bool
	}{
		{
			name: "Compare hand 2 is stronger because of lower level type",
			h1:   NewHand("AAAAA", 0),
			h2:   NewHand("AAAAK", 0),
			res:  false,
		},
		{
			name: "Compare hand 2 is not stroner because of higher level type",
			h1:   NewHand("33321", 0),
			h2:   NewHand("33322", 0),
			res:  true,
		},
		{
			name: "Compare hand 2 is stronger because 4 is greater than 2",
			h1:   NewHand("33321", 0),
			h2:   NewHand("33342", 0),
			res:  true,
		},
		{
			name: "Hand 1 is stronger because K > Q",
			h1:   NewHand("AAAKA", 0),
			h2:   NewHand("AAAQA", 0),
			res:  false,
		},
		{
			name: "Hand 1 is stronger because second K > T",
			h1:   NewHand("KK677", 0),
			h2:   NewHand("KTJJT", 0),
			res:  false,
		},
		{
			name: "Hand 1 is stronger because K > 3",
			h1:   NewHand("24K3A", 0),
			h2:   NewHand("24386", 0),
			res:  false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			res := tt.h1.Cmp(tt.h2)
			if res != tt.res {
				t.Errorf("got: %t, exteded: %t", res, tt.res)
			}
		})
	}
}

func Test_CalcBestVersion(t *testing.T) {
	tests := []struct {
		name string
		in   string
		out  string
	}{
		{"without Js best is the same as input", "23456", "23456"},
		{"form four of 5s", "T55J5", "T5555"},
		{"form three of 3s", "T23J3", "T2333"},
		{"form three of 5s because it is higher than 4", "5544J", "55445"},
		{"without pairs choose the highest possible value and form pair", "J3456", "63456"},
		{"without pairs and multiple Js choose the highest possible value to form Three", "J34J6", "63466"},
		{"without pairs and multiple Js choose the highest possible value to form Four", "J34JJ", "43444"},
		{"with all Js go to higest possible five of a kidn", "JJJJJ", "AAAAA"},
		{"if there is only one other card - join it to form a Five", "JJJJ2", "22222"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			h := NewHand(tt.in, 0)
			res := h.CalcBestVersion()
			if res != tt.out {
				t.Errorf("got: %s, exteded: %s", res, tt.out)
			}
		})
	}
}

func Test_CmpBestVersion(t *testing.T) {
	tests := []struct {
		name  string
		hand  string
		other string
		res   bool
	}{
		{"Expect K(ing) to be stroner than Q(ueen)", "KTJJT", "QQQJA", false},
		{"Expect T(en) to be stroner than J even though they both resolve to 5 Ts", "JJJJT", "TJJJJ", true},
		{"Expect K(ing) to be stroner than J even when it resolves to Q", "2K688", "2J68Q", false},
		{"JKKK2 is weaker than QQQQ2 because because J is weaker than Q", "QQQQ2", "JKKK2", false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			h := NewHand(tt.hand, 0)
			other := NewHand(tt.other, 0)
			res := h.CmpBestVersion(other)
			if res != tt.res {
				t.Errorf("got: %t, exteded: %t", res, tt.res)
			}
		})
	}
}
