class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the `MinStack` class:

    - `MinStack()` initializes the stack object.
    - `void push(int val)` pushes the element val onto the stack.
    - `void pop()` removes the element on the top of the stack.
    - `int top()` gets the top element of the stack.
    - `int getMin()` retrieves the minimum element in the stack.
    
    You must implement a solution with `O(1)` time complexity for each function.
    """

    def __init__(self):
        # The first stack is the stack for keeping track of the values
        # Second stack is to keep record of the minimum value in the first stack
        self.stack: list[int] = []
        self.minStack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]