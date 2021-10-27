class Solution:
    def totalNQueens(self, n: int) -> int:
        single_solution = [["." for _ in range(n)] for _ in range(n)]
        visited_col_set = set()
        diagonal_set = set()
        anti_diagonal_set = set()

        def dfs(row):
            if row == n:
                return 1
            result = 0
            for col in range(n):
                diagonal = col - row
                anti_diagonal = col + row
                if (
                    col not in visited_col_set
                    and diagonal not in diagonal_set
                    and anti_diagonal not in anti_diagonal_set
                ):
                    single_solution[row][col] = "Q"
                    visited_col_set.add(col)
                    diagonal_set.add(diagonal)
                    anti_diagonal_set.add(anti_diagonal)
                    result += dfs(row + 1)
                    anti_diagonal_set.remove(anti_diagonal)
                    diagonal_set.remove(diagonal)
                    visited_col_set.remove(col)
                    single_solution[row][col] = "."
            return result

        return dfs(0)


if __name__ == "__main__":
    solution = Solution()
    for i in range(1, 9):
        print(i, solution.totalNQueens(i))
