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
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []

        def backtrack(sub: str = "", i: int = 0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)

        backtrack()

        return res


if __name__ == "__main__":
    s = Solution()

    # Examples
    res1 = s.letterCasePermutation("a1b2")
    res2 = s.letterCasePermutation("3z4")
    res3 = s.letterCasePermutation("12345")

    assert all(i in res1 for i in ["a1b2", "a1B2", "A1b2", "A1B2"])
    assert all(i in res2 for i in ["3z4", "3Z4"])
    assert all(i in res3 for i in ["12345"])
