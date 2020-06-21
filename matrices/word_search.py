"""Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

"""
from typing import List


class Solution:
    # Time complexity: O(m * n * 4 ^ s)
    # Space complexity: O(1)
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word):
                    return True

        return False

    def dfs(self, board, row, col, word):
        if not word:
            return True

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False

        if word[0] != board[row][col]:
            return False

        char = board[row][col]
        board[row][col] = "#"

        res = (
            self.dfs(board, row + 1, col, word[1:])
            or self.dfs(board, row - 1, col, word[1:])
            or self.dfs(board, row, col + 1, word[1:])
            or self.dfs(board, row, col - 1, word[1:])
        )

        board[row][col] = char

        return res


if __name__ == "__main__":
    S = Solution()

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    # Example 1
    word = "ABCCED"
    assert S.exist(board, word) is True

    # Example 1
    word = "SEE"
    assert S.exist(board, word) is True

    # Example 1
    word = "ABCB"
    assert S.exist(board, word) is False

    print("All tests passed.")
