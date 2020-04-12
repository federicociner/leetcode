"""Given two strings S and T, return if they are equal when both are typed
into empty text editors. # means a backspace character.

Example 1:

    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2:

    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3:

    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4:

    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?

"""
from itertools import zip_longest


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = self.addBackspace(S)
        b = self.addBackspace(T)

        return all(x == y for x, y in zip_longest(a, b))

    def addBackspace(self, s: str):
        skip = 0

        for c in reversed(s):
            if c == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield c


if __name__ == "__main__":
    s = Solution()

    # Example 1
    S = "ab#c"
    T = "ad#c"
    assert s.backspaceCompare(S, T) is True

    # Example 2
    S = "ab##"
    T = "c#d#"
    assert s.backspaceCompare(S, T) is True

    # Example 3
    S = "a##c"
    T = "#a#c"
    assert s.backspaceCompare(S, T) is True

    # Example 4
    S = "a#c"
    T = "b"
    assert s.backspaceCompare(S, T) is False

    print("All tests passed.")
