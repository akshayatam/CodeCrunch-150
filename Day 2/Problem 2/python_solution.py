class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a set of vowels for easy lookup
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        # Convert the string into a list to allow modification
        s = list(s)
        # Initialize two pointers, one at the start and one at the end of the list
        left, right = 0, len(s) - 1
        
        # Continue looping until the two pointers meet
        while left < right:
            # Move the left pointer forward if it's not pointing at a vowel
            while left < right and s[left].lower() not in vowels:
                left += 1
            # Move the right pointer backward if it's not pointing at a vowel
            while left < right and s[right].lower() not in vowels:
                right -= 1

            # Swap the vowels pointed by left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move both pointers towards the center
            left += 1
            right -= 1

        # Join the list back into a string and return it
        return "".join(s)

def main():
    solution = Solution()
    print(solution.reverseVowels("hello"))  # Output: "holle"
    print(solution.reverseVowels("leetcode"))  # Output: "leotcede"

if __name__ == "__main__":
    main()
