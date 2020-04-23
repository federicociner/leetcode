"""Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:

    Input: "cbbd"
    Output: "bb"

"""


class SolutionA:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n ^ 2)
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s

        # start and end positions of result
        start = 0
        end = 0

        # initialise 2D table
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i] = True

        # fill out DP table by solving subproblems
        for i in range(n):
            for j in range(i, -1, -1):
                same_start_end = s[i] == s[j]

                if i == j:
                    # same character: "a" is a palindrome
                    dp[i][j] = True
                elif i - j == 1:
                    # if length 2, "ab" is palindrome if "a" == "b"
                    dp[i][j] = same_start_end
                elif same_start_end and dp[i - 1][j + 1]:
                    # string is palindrome if s(i) == s(j) and substring
                    # s(j + 1, i - 1) is a palindrome
                    dp[i][j] = True

                if dp[i][j] and i - j > end - start:
                    end = i
                    start = j

        return s[start: end + 1]


class SolutionB:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s

        # base case
        longest = s[0]

        for i in range(len(s)):
            # initial expand from center
            curr = self.expand(s, i, i)
            if len(curr) > len(longest):
                longest = curr

            # check if substring has two centers, e.g. "abba"
            curr = self.expand(s, i, i + 1)
            if len(curr) > len(longest):
                longest = curr

        return longest

    def expand(self, s: str, start: int, end: int) -> str:
        while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
            start -= 1
            end += 1

        return s[start + 1: end]


if __name__ == "__main__":
    s = SolutionB()

    # Example 1
    S = "babad"
    assert s.longestPalindrome(S) == "bab"

    # Example 2
    S = "cbbd"
    assert s.longestPalindrome(S) == "bb"

    # Example 3
    S = "bb"
    assert s.longestPalindrome(S) == "bb"

    # Example 4
    S = "ccc"
    assert s.longestPalindrome(S) == "ccc"

    print("All tests passed.")
