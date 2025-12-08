package leetcode1523

import ()

func countOdds(low int, high int) int {
	if low%2 == 0 && high%2 == 0 {
		return (high - low) / 2
	} else {
		return (high-low)/2 + 1
	}
}
