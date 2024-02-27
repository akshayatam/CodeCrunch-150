class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Define a lambda function for calculating the greatest common divisor (GCD)
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        
        # Check if str1 and str2 are concatenations of some common substring
        if (str1 + str2 == str2 + str1):
            # Calculate the GCD of the lengths of str1 and str2
            x = gcd(len(str1), len(str2))
            # Return the largest common substring that divides both str1 and str2
            return str1[:x]        
        else:
            # Return an empty string if no common dividing substring is found
            return ''

# Main function to test the Solution class
def main():
    solution = Solution()
    # Example 1
    print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
    # Example 2
    print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
    # Example 3
    print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""

if __name__ == "__main__":
    main()
