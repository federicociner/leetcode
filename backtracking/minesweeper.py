"""You are given a 2D char matrix representing the game board. 'M' represents
an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents
a revealed blank square that has no adjacent (above, below, left, right, and
all 4 diagonals) mines, digit ('1' to '8') represents how many mines are
adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the
unrevealed squares ('M' or 'E'), return the board after revealing this
position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.

If an empty square ('E') with no adjacent mines is revealed, then change it to
revealed blank ('B') and all of its adjacent unrevealed squares should be
revealed recursively.

If an empty square ('E') with at least one adjacent mine is revealed, then
change it to a digit ('1' to '8') representing the number of adjacent mines.

Return the board when no more squares will be revealed.


Example 1:

    Input:

    [['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'M', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E']]

    Click : [3,0]

    Output:

    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]

Example 2:

    Input:

    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]

    Click : [1,2]

    Output:

    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'X', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]

"""
from typing import List


class Solution:
    def updateBoard(
        self, board: List[List[str]], click: List[int]
    ) -> List[List[str]]:
        x = click[0]
        y = click[1]

        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return

        if board[x][y] == "M":
            board[x][y] = "X"

            return board
        elif board[x][y] == "E":
            num_adj_mines = self.num_adj_mines(board, x, y)

            if num_adj_mines:
                board[x][y] = str(num_adj_mines)
            else:
                board[x][y] = "B"
                self.updateBoard(board, [x + 1, y])
                self.updateBoard(board, [x, y + 1])
                self.updateBoard(board, [x - 1, y])
                self.updateBoard(board, [x, y - 1])
                self.updateBoard(board, [x + 1, y + 1])
                self.updateBoard(board, [x + 1, y - 1])
                self.updateBoard(board, [x - 1, y + 1])
                self.updateBoard(board, [x - 1, y - 1])

            return board

    def num_adj_mines(self, board: List[List[str]], x: int, y: int) -> int:
        def is_mine(x: int, y: int) -> int:
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                return 0

            if board[x][y] == "M":
                return 1

            return 0

        num_adj_mines = (
            is_mine(x + 1, y)
            + is_mine(x - 1, y)
            + is_mine(x, y + 1)
            + is_mine(x, y - 1)
            + is_mine(x + 1, y + 1)
            + is_mine(x + 1, y - 1)
            + is_mine(x - 1, y + 1)
            + is_mine(x - 1, y - 1)
        )

        return num_adj_mines


if __name__ == "__main__":
    s = Solution()

    # Example 1
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    click = [3, 0]
    actual = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    expected = s.updateBoard(board, click)

    assert actual == expected

    # Example 2
    board = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]

    click = [1, 2]
    actual = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "X", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    expected = s.updateBoard(board, click)

    assert actual == expected
