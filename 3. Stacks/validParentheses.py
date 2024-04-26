def isValidParentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    """
    stack: list[str] = []
    closeToOpen: dict[str,str] = {")" : "(",
                                  "]" : "[",
                                  "}" : "{"}
    
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False 
        else:
            stack.append(c)
            
    return True if not stack else False 

def main():
    tests: list[str] = ["()", "()[]{}", "(]"]

    for test in tests:
        print(isValidParentheses(test))

if __name__ == "__main__":
    main()