class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Initialize a flag to check if the previous plot is planted
        # If the first plot is empty, set flag to False (indicating we can potentially plant a flower)
        flag = False if flowerbed[0] == 0 else True
        
        # Iterate through the flowerbed except the last plot
        for i in range(len(flowerbed) - 1):
            # Check if the current and next plots are empty and we haven't just planted a flower
            if not flowerbed[i] and not flowerbed[i + 1] and not flag:
                # Plant a flower by decrementing n and setting flag to True
                n -= 1
                flag = True
            elif not flowerbed[i]:
                # If current plot is empty and we didn't plant a flower, reset flag to False
                flag = False
            else:
                # If current plot is not empty, ensure flag is True
                flag = True
                
        # After loop, check the last plot if it's possible to plant
        if not flag and not flowerbed[-1]:
            n -= 1
            
        # If n is more than 0, return False, else True
        return n <= 0

# Main function with examples
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers([1,0,0,0,1], 1))  # Expected output: True
    print(sol.canPlaceFlowers([1,0,0,0,1], 2))  # Expected output: False
