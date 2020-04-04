"""Given a string S, we can transform every letter individually to be
lowercase or uppercase to create another string.  Return a list of all
possible strings we could create.

Examples:
    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: S = "3z4"
    Output: ["3z4", "3Z4"]

    Input: S = "12345"
    Output: ["12345"]

Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

"""
from typing import List


class Solution:
    # Time complexity: O(2^n * n)
    # Space complexity: O(2^n * n)
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.backtrack(S, 0, "", res)

        return res

    def backtrack(self, S: str, idx: int, sub: str, res: List[str]):
        # substring length is equal to length of S, all characters traversed
        if idx == len(S):
            res.append(sub)

            return

        # not alphabetical => one backtrack call
        if S[idx].lower() == S[idx].upper():
            self.backtrack(S, idx + 1, sub + S[idx], res)

        # alphabetical => two backtrack calls
        else:
            self.backtrack(S, idx + 1, sub + S[idx].upper(), res)
            self.backtrack(S, idx + 1, sub + S[idx].lower(), res)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    res = s.letterCasePermutation("a1b2")
    assert all(i in res for i in ["a1b2", "a1B2", "A1b2", "A1B2"])

    # Example 2
    res = s.letterCasePermutation("12345")
    assert all(i in res for i in ["12345"])

    # Example 3
    res = s.letterCasePermutation("3z4")
    assert all(i in res for i in ["3z4", "3Z4"])

    print("All tests passed.")
