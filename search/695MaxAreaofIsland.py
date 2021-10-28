from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        BFS
        """
        visited_set = set()
        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited_set:
                    queue = deque([(i, j)])
                    visited_set.add((i, j))
                    area = 0
                    while queue:
                        c_i, c_j = queue.pop()
                        area += 1
                        for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            new_i, new_j = c_i + delta_i, c_j + delta_j
                            if (
                                0 <= new_i < m
                                and 0 <= new_j < n
                                and grid[new_i][new_j]
                                and (new_i, new_j) not in visited_set
                            ):
                                visited_set.add((new_i, new_j))
                                queue.appendleft((new_i, new_j))
                    max_area = max(max_area, area)
        return max_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        DFS
        """
        visited_set = set()
        max_area = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            visited_set.add((i, j))
            area = 0
            for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i, new_j = i + delta_i, j + delta_j
                if (
                    0 <= new_i < m
                    and 0 <= new_j < n
                    and grid[new_i][new_j]
                    and (new_i, new_j) not in visited_set
                ):
                    area += dfs(new_i, new_j)
            return 1 + area

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited_set:
                    max_area = max(max_area, dfs(i, j))
        return max_area


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maxAreaOfIsland(
            grid=[
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
    )
    print(
        solution.maxAreaOfIsland(
            grid=[
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
    )
    print(solution.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))
