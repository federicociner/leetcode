"""Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

For example, given n = 3, a solution set is:

    [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generateParenthesis(n, n, "", res)

        return res

    def backtrack(
        self, left: int, right: int, sub: List[str], res: List[List[str]]
    ):
        pass


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.generateParenthesis(3)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)
