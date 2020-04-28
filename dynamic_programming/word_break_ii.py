"""Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is a
valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation. You may assume the dictionary does not contain duplicate words.

Example 1:

    Input:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    Output:
    [
    "cats and dog",
    "cat sand dog"
    ]

Example 2:

    Input:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    Output:
    [
    "pine apple pen apple",
    "pineapple pen apple",
    "pine applepen apple"
    ]
    Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

    Input:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output:
    []

"""
from typing import List


class Solution:
    # Time complexity: O(n * n ^ 2)
    # Space complexity: O(n ^ 2)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        self.dfs(s, wordDict, "", ans)

        return ans

    def dfs(
        self, s: str, wordDict: List[str], sub: str, ans: List[str]
    ) -> None:
        # check if remaining string can  be split using wordDict
        if self.isValidString(s, wordDict):
            if not s:
                ans.append(sub[:-1])  # exclude trailing space

                return

            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, sub + s[:i] + " ", ans)

    def isValidString(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        # base case
        dp[0] = True

        # build DP table
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]


if __name__ == "__main__":
    S = Solution()

    # Example 1
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    expected = ["cats and dog", "cat sand dog"]
    actual = S.wordBreak(s, wordDict)

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    # Example 2
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected = [
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple",
    ]
    actual = S.wordBreak(s, wordDict)

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    # Example 3
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    expected = []
    actual = S.wordBreak(s, wordDict)

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
