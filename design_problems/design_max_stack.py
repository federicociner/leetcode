"""Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you f
ind more than one maximum elements, only remove the top-most one.

Example 1:
    MaxStack stack = new MaxStack();
    stack.push(5);
    stack.push(1);
    stack.push(5);
    stack.top(); -> 5
    stack.popMax(); -> 5
    stack.top(); -> 1
    stack.peekMax(); -> 5
    stack.pop(); -> 1
    stack.top(); -> 5

Note:
    * -1e7 <= x <= 1e7
    * Number of operations won't exceed 10000.
    * The last four operations won't be called when stack is empty.

"""


class MaxStack:
    # Time complexity: O(1), except popMax() which is O(n)
    # Space complexity: O(n)
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        m = max(x, self.stack[-1][1] if self.stack else float("-inf"))
        self.stack.append([x, m])

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        m = self.stack[-1][1]
        b = []

        while self.stack[-1][0] != m:
            b.append(self.pop())

        self.pop()
        for item in reversed(b):
            self.push(item)

        return m


if __name__ == "__main__":
    S = MaxStack()

    # Example 1
    S.push(5)
    S.push(1)
    S.push(5)
    assert S.top() == 5
    assert S.popMax() == 5
    assert S.top() == 1
    assert S.peekMax() == 5
    assert S.pop() == 1
    assert S.top() == 5

    # Example 2
    S = MaxStack()
    S.push(5)
    S.push(1)
    assert S.popMax() == 5
    assert S.peekMax() == 1

    print("All tests passed.")
