def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Create hashmap of distinct values and count
    count: dict[int,int] = {}

    # Create a frequency list that stores count and what number has that count
    freq: list[list[int]] = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    for n, c in count.items():
        freq[c].append(n)
    
    res: list[int] = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)

            if len(res) == k:
                return res


def main():
    nums: list[list[int]] = [[1,1,1,2,2,3], [1]]
    k: list[int] = [2, 1]

    for i in range(len(nums)):
        print(topKFrequent(nums[i], k[i]))

if __name__ == "__main__":
    main()