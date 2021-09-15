from typing import List
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_set = defaultdict(set)
        column_set = defaultdict(set)
        square_set = defaultdict(set)
        m, n = len(board), len(board[0])
        missing_position_list = []
        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    row_set[i].add(board[i][j])
                    column_set[j].add(board[i][j])
                    square_set[i // 3 * 3 + j // 3].add(board[i][j])
                else:
                    missing_position_list.append((i, j))

        def dfs(i):
            if i == len(missing_position_list):
                return True
            row, col = missing_position_list[i]
            for num in range(1, 10):
                num = str(num)
                if (
                    num not in row_set[row]
                    and num not in column_set[col]
                    and num not in square_set[row // 3 * 3 + col // 3]
                ):
                    row_set[row].add(num)
                    column_set[col].add(num)
                    square_set[row // 3 * 3 + col // 3].add(num)
                    solvable = dfs(i + 1)
                    board[row][col] = num
                    if solvable:
                        return True
                    board[row][col] = "."
                    row_set[row].remove(num)
                    column_set[col].remove(num)
                    square_set[row // 3 * 3 + col // 3].remove(num)

        dfs(0)
        print(board)


if __name__ == "__main__":
    solution = Solution()
    solution.solveSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
