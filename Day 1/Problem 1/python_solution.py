class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers for both strings
        ptr1 = 0
        ptr2 = 0

        # Initialize the merged string
        merged = ''

        # Find the length of the shorter string to ensure equal alternation
        n = min(len(word1), len(word2))

        # Loop through both strings up to the length of the shorter string
        for _ in range(n):
            # Add the current character from word1 to the merged string
            merged += word1[ptr1]
            ptr1 += 1  # Move to the next character in word1

            # Add the current character from word2 to the merged string
            merged += word2[ptr2]
            ptr2 += 1  # Move to the next character in word2

        # After merging characters alternately up to the shorter length,
        # append the remaining characters of the longer string.
        if len(word1) > len(word2):
            return merged + word1[ptr1:]  # Append remaining characters from word1
        return merged + word2[ptr2:]  # Append remaining characters from word2

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Example 1
    word1 = "abc"
    word2 = "pqr"
    print("Example 1 Output:", solution.mergeAlternately(word1, word2))
    
    # Example 2
    word1 = "ab"
    word2 = "pqrs"
    print("Example 2 Output:", solution.mergeAlternately(word1, word2))
    
    # Example 3
    word1 = "abcd"
    word2 = "pq"
    print("Example 3 Output:", solution.mergeAlternately(word1, word2))

if __name__ == "__main__":
    main()
