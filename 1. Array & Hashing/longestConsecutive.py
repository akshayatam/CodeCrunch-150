def longestConsecutive(nums: list[int]) -> int:
    numSet: set = set(nums)
    longest: int = 0

    for n in nums:
        # Check if start of sequence
        if (n - 1) not in nums:
            length: int = 0

            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

def main():
    tests: list[list[int]] = [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]

    for test in tests:
        print(longestConsecutive(test))

if __name__ == "__main__":
    main()