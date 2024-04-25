def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """
    hashmap: dict[int,int] = {}

    for i, n in enumerate(nums):
        diff = target - n 

        if diff in hashmap:
            return [hashmap[diff], i]
        
        hashmap[n] = i

    return

def main():
    nums: list[list[int]] = [[2,7,11,15], [3,2,4], [3,3]]
    target: list[int] = [9, 6, 6]

    for i in range(len(nums)):
        print(twoSum(nums[i], target[i]))

if __name__ == "__main__":
    main()