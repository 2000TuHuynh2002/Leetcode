package leetcode2144

import (
	"slices"
)

func minimumCost(cost []int) int {
	slices.Sort(cost)
	slices.Reverse(cost)

	total := 0
	for idx, val := range cost {
		if idx % 3 != 2 {
			total += val
		}
	}

	return total
}