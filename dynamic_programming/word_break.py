"""Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

    - The same word in the dictionary may be reused multiple times in the
    segmentation.
    - You may assume the dictionary does not contain duplicate words.

Example 1:

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet
    code".

Example 2:

    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as
    "apple pen apple".

    Note that you are allowed to reuse a dictionary word.

Example 3:

    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false

"""
from typing import List


class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
    s = "leetcode"
    wordDict = ["leet", "code"]
    assert S.wordBreak(s, wordDict) is True

    # Example 2
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    assert S.wordBreak(s, wordDict) is True

    # Example 3
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    assert S.wordBreak(s, wordDict) is False

    print("All tests passed.")
