"""Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

"""


class MinStack:
    # Time complexity of operations: O(1)
    # Space complexity: O(n)
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)

        self.stack.append(x)

    def pop(self) -> None:
        ans = self.stack.pop()

        if ans == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


if __name__ == "__main__":
    # Example
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2

    print("All tests passed.")
