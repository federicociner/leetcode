"""Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

    Input: "word"
    Output:
    [
        "word",
        "1ord",
        "w1rd",
        "wo1d",
        "wor1",
        "2rd",
        "w2d",
        "wo2",
        "1o1d",
        "1or1",
        "w1r1",
        "1o2",
        "2r1",
        "3d",
        "w3",
        "4"
    ]

"""
from typing import List


class Solution:
    # Time complexity: O(n * 2^n)
    # Space complexity: O(n)
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []
        self.backtrack(word, 0, 0, "", ans)

        return ans

    def backtrack(
        self, word: str, index: int, k: int, sub: str, ans: List[str]
    ) -> None:
        if index == len(word):
            if k != 0:
                sub += str(k)
            ans.append(sub)
        else:
            self.backtrack(word, index + 1, k + 1, sub, ans)

            if k != 0:
                sub += str(k)

            sub += word[index]
            self.backtrack(word, index + 1, 0, sub, ans)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    word = "word"
    actual = s.generateAbbreviations(word)
    expected = [
        "word",
        "1ord",
        "w1rd",
        "wo1d",
        "wor1",
        "2rd",
        "w2d",
        "wo2",
        "1o1d",
        "1or1",
        "w1r1",
        "1o2",
        "2r1",
        "3d",
        "w3",
        "4",
    ]

    assert len(actual) == len(expected)
    assert all(i in actual for i in expected)

    print("All tests passed.")
