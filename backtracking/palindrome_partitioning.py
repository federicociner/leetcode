"""Given a string s, partition s such that every substring of the partition is
a palindrome.

Return all possible palindrome partitioning of s.

Example:

    Input: "aab"
    Output:
    [
        ["aa","b"],
        ["a","a","b"]
    ]

"""
from typing import List


class Solution:
    # Time complexity: O(n * 2^n)
    # Space complexity: O(n * 2^n)
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.backtrack(s, [], ans)

        return ans

    def backtrack(self, s: str, sub: str, ans: [List[List[str]]]) -> None:
        if not s:
            ans.append(sub)

        for i in range(0, len(s)):
            if self.is_palindrome(s[: i + 1]):
                self.backtrack(s[i + 1 :], sub + [s[: i + 1]], ans)

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.partition("aab")
    expected = [["aa", "b"], ["a", "a", "b"]]

    assert len(expected) == len(actual)
    assert all(i for i in actual for i in expected)

    print("All tests passed.")
