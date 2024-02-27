package main

import (
	"fmt"
	"strings"
)

// ReverseWords reverses the words in the string `s`.
func ReverseWords(s string) string {
	// Split the string into words, then reverse the slice of words.
	words := strings.Fields(s)
	for i, j := 0, len(words)-1; i < j; i, j = i+1, j-1 {
		words[i], words[j] = words[j], words[i]
	}
	// Join the reversed slice of words back into a string with a space separator.
	return strings.Join(words, " ")
}

func main() {
	// Example 1
	example1 := "the sky is blue"
	fmt.Printf("Input: '%s'\nOutput: '%s'\n", example1, ReverseWords(example1))

	// Example 2
	example2 := "  hello world  "
	fmt.Printf("\nInput: '%s'\nOutput: '%s'\n", example2, ReverseWords(example2))

	// Example 3
	example3 := "a good   example"
	fmt.Printf("\nInput: '%s'\nOutput: '%s'\n", example3, ReverseWords(example3))
}
