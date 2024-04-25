from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list) # Mapping character count to list of anagrams

    for s in strs:
        count = [0] * 26 # a to z

        for c in s:
            count[ord(c) - ord("a")] += 1
        
        res[tuple(count)].append(s)
    
    return res.values()

def main():
    tests: list[list[str]] = [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]

    for test in tests:
        print(groupAnagrams(test))

if __name__ == "__main__":
    main()