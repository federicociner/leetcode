"""Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another
expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would
always evaluate to a result and there won't be any divide by zero operation.

Example 1:

    Input: ["2", "1", "+", "3", "*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

Example 2:

    Input: ["4", "13", "5", "/", "+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6

Example 3:

    Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "
    +"]
    Output: 22
    Explanation:
    ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

"""
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack = []

        for token in tokens:
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                res = operators[token](a, b)
                stack.append(res)
            else:
                stack.append(token)

        return stack.pop()


if __name__ == "__main__":
    S = Solution()

    # Example 1
    tokens = ["2", "1", "+", "3", "*"]
    assert S.evalRPN(tokens) == 9

    # Example 2
    tokens = ["4", "13", "5", "/", "+"]
    assert S.evalRPN(tokens) == 6

    # Example 3
    tokens = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "/",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]
    assert S.evalRPN(tokens) == 22

    print("All tests passed.")
