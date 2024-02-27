class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Find the maximum number of candies any kid currently has
        max_candies = max(candies)
        
        # Initialize an empty list to store the result
        result = []
        
        # Iterate over each kid
        for c in candies:
            # Check if adding extraCandies to the current kid's candies
            # makes their total greater than or equal to max_candies
            if c + extraCandies >= max_candies:
                result.append(True)  # Kid can have the greatest number of candies
            else:
                result.append(False)  # Kid cannot have the greatest number of candies
        
        # Return the result list
        return result

# Main function to test the solution with provided examples
if __name__ == "__main__":
    sol = Solution()
    print(sol.kidsWithCandies([2,3,5,1,3], 3))  # Example 1
    print(sol.kidsWithCandies([4,2,1,1,2], 1))  # Example 2
    print(sol.kidsWithCandies([12,1,12], 10))   # Example 3