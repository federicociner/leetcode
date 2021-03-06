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
    # Time complexity: O(4n / sqrt(n))
    # Space complexity: O(4n / sqrt(n))
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(n, n, "", res)

        return res

    def backtrack(
        self, left: int, right: int, sub: List[str], res: List[List[str]]
    ) -> None:
        if right < left:
            return

        if left == 0 and right == 0:
            res.append(sub)

        if left > 0:
            self.backtrack(left - 1, right, sub + "(", res)
        if right > 0:
            self.backtrack(left, right - 1, sub + ")", res)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.generateParenthesis(3)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
