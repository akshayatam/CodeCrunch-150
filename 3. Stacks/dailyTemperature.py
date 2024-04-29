def dailyTemperature(temperatures: list[int]) -> list[int]:
    stack: list[list[int]] = [] # pair: [temp, index]
    answer: list[int] = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            answer[stackInd] = (i - stackInd)
        
        stack.append([t,i])
    return answer
        

def main():
    tests: list[list[int]] = [[73,74,75,71,69,72,76,73], [30,40,50,60], [30,60,90]]

    for test in tests:
        print(dailyTemperature(test))

if __name__ == "__main__":
    main()