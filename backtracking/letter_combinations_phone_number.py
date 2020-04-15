"""Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

Example:

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""
from itertools import zip_longest
from typing import List, Dict


class Solution:
    # Time complexity: O(3^n * 4^m)
    # Space complexity: O(3^n * 4^m)
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits:
            self.backtrack(mapping, digits, "", ans)

        return ans

    def backtrack(
        self, mapping: Dict[str, str], digits: str, sub: str, ans: List[str]
    ) -> None:
        if len(digits) == 0:
            ans.append(sub)

            return

        for letter in mapping[digits[0]]:
            self.backtrack(mapping, digits[1:], sub + letter, ans)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    digits = "23"
    actual = s.letterCombinations(digits)
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    assert len(actual) == len(expected)
    assert all(x == y for x, y in zip_longest(actual, expected))

    print("All tests passed.")
