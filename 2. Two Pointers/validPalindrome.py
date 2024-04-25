def isPalindrome(s: str) -> bool:
    left: int = 0
    right: int = len(s) - 1

    while left < right:
        while left < right and not isAlpha(s[left]):
            left += 1  
        while right > left and not isAlpha(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def isAlpha(c: str) -> bool:
    return (
        ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9')
    )

def main():
    tests: list[str] = ["A man, a plan, a canal: Panama", 
                        "race a car",
                        " "]

    for test in tests:
        print(isPalindrome(test))
    
if __name__ == "__main__":
    main()