class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string `s` into words. This automatically removes all leading, trailing,
        # and in-between spaces, leaving only the words.
        words = s.split()
        
        # Reverse the list of words.
        reversed_words = words[::-1]
        
        # Join the reversed list of words back into a string with a single space separating them.
        reversed_string = " ".join(reversed_words)
        
        # Return the reversed string.
        return reversed_string

# Main function to test the Solution class with the provided examples
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    example1 = "the sky is blue"
    print(f"Input: '{example1}'")
    print(f"Output: '{solution.reverseWords(example1)}'")
    
    # Example 2
    example2 = "  hello world  "
    print(f"\nInput: '{example2}'")
    print(f"Output: '{solution.reverseWords(example2)}'")
    
    # Example 3
    example3 = "a good   example"
    print(f"\nInput: '{example3}'")
    print(f"Output: '{solution.reverseWords(example3)}'")
