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
    def partition(self, s: str) -> List[List[str]]:
        pass


if __name__ == "__main__":
    s = Solution()

    # Example 1
    actual = s.partition("aab")
    expected = [["aa", "b"], ["a", "a", "b"]]

    assert len(expected) == len(actual)
    assert all(i for i in actual for i in expected)
