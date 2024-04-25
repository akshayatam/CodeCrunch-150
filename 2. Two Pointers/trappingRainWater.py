def trap(height: list[int]) -> int:
    """
    Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.
    """
    # Edge case
    if not height:
        return 0

    left: int = 0
    right: int = len(height) - 1

    leftMax: int = height[left]
    rightMax: int = height[right]

    res: int = 0

    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, height[left])
            res += leftMax - height[left]
        else:
            right -= 1
            rightMax = max(rightMax, height[right])
            res += rightMax - height[right]
    
    return res

def main():
    tests: list[list[int]] = [[0,1,0,2,1,0,1,3,2,1,2,1], [4,2,0,3,2,5]]

    for test in tests:
        print(trap(test))

if __name__ == "__main__":
    main()