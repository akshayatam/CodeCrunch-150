package main

import "fmt"

// canPlaceFlowers checks if n new flowers can be planted in the flowerbed
// without violating the no-adjacent-flowers rule.
func canPlaceFlowers(flowerbed []int, n int) bool {
	// Initialize flag to track the planting status of the previous plot.
	flag := false
	if flowerbed[0] == 0 {
		flag = false // First plot is empty, might plant a flower here.
	} else {
		flag = true // First plot is not empty, cannot plant a flower here.
	}

	// Iterate over the flowerbed to find potential spots for planting.
	for i := 0; i < len(flowerbed)-1; i++ {
		// Check if current and next plots are empty and no recent flower was planted.
		if flowerbed[i] == 0 && flowerbed[i+1] == 0 && !flag {
			n--         // Plant a flower.
			flag = true // Update flag since we just planted a flower.
		} else if flowerbed[i] == 0 {
			flag = false // Current plot is empty, and we didn't plant a flower.
		} else {
			flag = true // Current plot is not empty.
		}
	}

	// Special case for the last plot in the flowerbed.
	if !flag && flowerbed[len(flowerbed)-1] == 0 {
		n-- // Plant a flower if possible.
	}

	// If n is 0 or negative, all flowers can be planted.
	return n <= 0
}

func main() {
	fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 1)) // Expected output: true
	fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 2)) // Expected output: false
}
