def evalRPN(tokens: list[str]) -> int:
    stack: list[int] = []

    for val in tokens:
        if val == "+":
            stack.append(stack.pop() + stack.pop())

        elif val == "-":
            a: int = stack.pop()
            b: int = stack.pop()
            stack.append(b - a)

        elif val == "*":
            stack.append(stack.pop() * stack.pop())

        elif val == "/":
            a: int = stack.pop()
            b: int = stack.pop()
            stack.append(int(b / a))
        
        else:
            stack.append(int(val))

    return stack[0]      
        
def main():
    tests: list[list[str]] = [["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]

    for test in tests:
        print(evalRPN(test))

if __name__ == "__main__":
    main()