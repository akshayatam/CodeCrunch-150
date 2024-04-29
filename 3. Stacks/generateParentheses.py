def generateParentheses(n: int) -> list[str]:
    """
    Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    """

    # Conditions
    # Only add open parentheses if open < n
    # Only add closed parentheses if closed < open
    # Solution valid iff open == closed == n

    stack: list[str] = []
    res: list[str] = []

    # Recursive function
    def backtrack(openN: int, closedN: int) -> None:
        # Base case
        if openN == closedN == n:
            res.append("".join(stack))
            return 
        
        # Condition to add open parentheses
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        
        # Condition to add closed parentheses
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    
    backtrack(0, 0)
    return res

def main():
    tests: list[int] = [3, 1]

    for test in tests: 
        print(generateParentheses(test))

if __name__ == "__main__":
    main()