package main

import (
	"fmt"
)

// Function to find kids with the greatest number of candies
func kidsWithCandies(candies []int, extraCandies int) []bool {
	maxCandies := 0
	// Find the maximum number of candies any kid currently has
	for _, c := range candies {
		if c > maxCandies {
			maxCandies = c
		}
	}

	result := make([]bool, len(candies))
	// Iterate over each kid
	for i, c := range candies {
		// Check if adding extraCandies makes the kid have the greatest number of candies
		if c+extraCandies >= maxCandies {
			result[i] = true
		} else {
			result[i] = false
		}
	}

	// Return the result slice
	return result
}

// Main function to test the solution with provided examples
func main() {
	fmt.Println(kidsWithCandies([]int{2, 3, 5, 1, 3}, 3)) // Example 1
	fmt.Println(kidsWithCandies([]int{4, 2, 1, 1, 2}, 1)) // Example 2
	fmt.Println(kidsWithCandies([]int{12, 1, 12}, 10))    // Example 3
}
