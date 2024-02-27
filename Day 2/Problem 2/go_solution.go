package main

import (
	"fmt"
	"strings"
)

// Checks if a character is a vowel
func isVowel(c rune) bool {
	return strings.ContainsRune("aeiouAEIOU", c)
}

// ReverseVowels reverses only the vowels in a string
func ReverseVowels(s string) string {
	runes := []rune(s)
	left, right := 0, len(runes)-1

	for left < right {
		// Find the next vowel from the left
		for left < right && !isVowel(runes[left]) {
			left++
		}
		// Find the next vowel from the right
		for left < right && !isVowel(runes[right]) {
			right--
		}
		// Swap the vowels
		runes[left], runes[right] = runes[right], runes[left]
		left++
		right--
	}

	return string(runes)
}

func main() {
	fmt.Println(ReverseVowels("hello"))    // Output: "holle"
	fmt.Println(ReverseVowels("leetcode")) // Output: "leotcede"
}
