"""Given a string containing just the characters '(' and ')', find the length
of the longest valid (well-formed) parentheses substring.

Example 1:

    Input: "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()"

Example 2:

    Input: ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()"

"""


class SolutionDP:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        curr_max = 0

        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
                    curr_max = max(dp[i], curr_max)
                else:
                    valid_index = (i - dp[i - 1] - 1) >= 0
                    if valid_index and s[i - dp[i - 1] - 1] == "(":
                        valid = (i - dp[i - 1] - 2) >= 0
                        prev = dp[i - dp[i - 1] - 2] if valid else 0
                        dp[i] = dp[i - 1] + 2 + prev
                        curr_max = max(dp[i], curr_max)

        return curr_max


class SolutionStack:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        dp = [0] * (len(s) + 1)
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1

        return max(dp)


if __name__ == "__main__":
    S = SolutionStack()

    # Example 1
    s = "(()"
    assert S.longestValidParentheses(s) == 2

    # Example 2
    s = ")()())"
    assert S.longestValidParentheses(s) == 4

    # Example 3
    s = ")()())()()("
    assert S.longestValidParentheses(s) == 4

    print("All tests passed.")
