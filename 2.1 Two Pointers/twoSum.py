def twoSum(numbers: list[int], target: int) -> list[int]:
    left: int = 0
    right: int = len(numbers) - 1

    while left < right:
        res: int = numbers[left] + numbers[right]

        if res == target:
            return [left+1, right+1]
        elif res > target:
            right -= 1
        elif res < target:
            left += 1
        

def main():
    nums: list[list[int]] = [[2,7,11,15], [2,3,4], [-1,0]]
    target: list[int] = [9, 6, -1]

    for i in range(len(nums)):
        print(twoSum(nums[i], target[i]))

if __name__ == "__main__":
    main()