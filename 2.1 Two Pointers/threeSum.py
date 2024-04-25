def threeSum(nums: list[int]) -> list[list[int]]:
    """
    Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

    Notice that the solution set must not contain duplicate triplets.
    """
    nums.sort()
    res: list[list[int]] = []
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l: int = i + 1
        r: int = len(nums) - 1
    
        while l < r:
            tot: int = a + nums[l] + nums[r]

            if tot > 0:
                r -= 1
            elif tot < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
        
    return res
    

def main():
    tests: list[list[int]] = [[-1,0,1,2,-1,-4], [0,1,1], [0,0,0]]

    for test in tests:
        print(threeSum(test))

if __name__ == "__main__":
    main()