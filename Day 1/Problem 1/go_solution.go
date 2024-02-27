package main

import "fmt"

// Function to merge strings alternately
func mergeAlternately(word1 string, word2 string) string {
	// Initialize an empty string to store the merged result
	res := ""

	// Determine the minimum length between word1 and word2
	minLen := min(len(word1), len(word2))

	// Iterate over the characters of both strings up to the minimum length
	for i := 0; i < minLen; i++ {
		// Append characters alternately from word1 and word2
		res += string(word1[i])
		res += string(word2[i])
	}

	// If word1 is longer than word2, append the remaining characters of word1
	if len(word1) > len(word2) {
		res += word1[minLen:]
	} else { // If word2 is longer than word1, append the remaining characters of word2
		res += word2[minLen:]
	}
	return res
}

// Function to find the minimum of two integers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	// Test cases
	word1 := "abc"
	word2 := "pqr"
	fmt.Println("Example 1:")
	fmt.Println("Input:", word1, ",", word2)
	fmt.Println("Output:", mergeAlternately(word1, word2)) // Expected output: "apbqcr"

	word1 = "ab"
	word2 = "pqrs"
	fmt.Println("\nExample 2:")
	fmt.Println("Input:", word1, ",", word2)
	fmt.Println("Output:", mergeAlternately(word1, word2)) // Expected output: "apbqrs"

	word1 = "abcd"
	word2 = "pq"
	fmt.Println("\nExample 3:")
	fmt.Println("Input:", word1, ",", word2)
	fmt.Println("Output:", mergeAlternately(word1, word2)) // Expected output: "apbqcd"
}
