def containsDuplicate(nums: list[int]) -> bool:
    '''
    Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.
    '''
    hashset: set = set()

    for n in nums:
        # Condition to check if key already in hashset
        if n in hashset:
            return True
        
        # Add the number to hashset
        hashset.add(n)
    return False
    
def main():
    tests: list[list[int]] = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
    for test in tests: 
        print(containsDuplicate(test))

if __name__ == "__main__":
    main()