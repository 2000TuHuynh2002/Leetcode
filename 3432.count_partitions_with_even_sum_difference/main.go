package leetcode3432

import ()

func sumArray(numbers []int) int {
	result := 0
	for i := 0; i < len(numbers); i++ {
		result += numbers[i]
	}
	return result
}

func countPartitions(nums []int) int {
	count := 0
	numsLength := len(nums)

	for i := 1; i < numsLength; i++ {
		if (sumArray(nums[:i])+sumArray(nums[i:numsLength]))%2 == 0 {
			count++
		}
	}

	return count
}
