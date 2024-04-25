def isAnagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    """
    if len(s) != len(t):
        return False
    
    res: dict[str, int] = {}
    res1: dict[str, int] = {}

    for i in range(len(s)):
        res[s[i]] = res.get(s[i], 0) + 1
        res1[t[i]] = res1.get(t[i], 0) + 1
    
    for c in res:
        if res[c] != res1.get(c, 0):
            return False
        
    return True

def main():
    tests: list[list[str]] = [["anagram", "nagaram"], ["rat", "car"]]

    for test in tests:
        print(isAnagram(test[0], test[1]))

if __name__ == "__main__":
    main()