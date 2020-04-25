"""A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of
ways to decode it.

Example 1:

    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2
    2 6).

"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # initialise DP table
        dp = [0] * (len(s) + 1)
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # one step jump
            if 0 < int(s[i - 1: i]) <= 9:
                dp[i] += dp[i - 1]
            # two step jump
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


if __name__ == "__main__":
    S = Solution()

    # Example 1
    s = "12"
    assert S.numDecodings(s) == 2

    # Example 2
    s = "226"
    assert S.numDecodings(s) == 3

    print("All tests passed.")
