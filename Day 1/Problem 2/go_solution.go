package main

import (
	"fmt"
)

func gcdOfStrings(str1 string, str2 string) string {
	// Function to calculate GCD of two numbers
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	// Check if str1 and str2 are concatenations of some common substring
	if str1+str2 == str2+str1 {
		// Calculate the GCD of the lengths of str1 and str2
		gcdLen := gcd(len(str1), len(str2))
		// Return the largest common substring that divides both str1 and str2
		return str1[:gcdLen]
	} else {
		// Return an empty string if no common dividing substring is found
		return ""
	}
}

func main() {
	// Example 1
	fmt.Println(gcdOfStrings("ABCABC", "ABC")) // Output: "ABC"
	// Example 2
	fmt.Println(gcdOfStrings("ABABAB", "ABAB")) // Output: "AB"
	// Example 3
	fmt.Println(gcdOfStrings("LEET", "CODE")) // Output: ""
}
