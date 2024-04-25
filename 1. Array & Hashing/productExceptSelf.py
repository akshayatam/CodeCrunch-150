def productExceptSelf(nums: list[int]) -> list[int]:
    res: list[int] = [1] * len(nums)

    # Prefix
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix 
        prefix *= nums[i]
    
    # Postfix
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res

def main():
    tests: list[list[int]] = [[1,2,3,4], [-1,1,0,-3,3]]
    
    for test in tests:
        print(productExceptSelf(test))

if __name__ == "__main__":
    main()