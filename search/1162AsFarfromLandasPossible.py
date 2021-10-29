from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue = deque([(i, j)])
                    level = 0
                    while queue:
                        queue_size = len(queue)
                        level += 1
                        for _ in range(queue_size):
                            c_i, c_j = queue.pop()
                            for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                new_i, new_j = c_i + delta_i, c_j + delta_j
                                if (
                                    0 <= new_i < m
                                    and 0 <= new_j < n
                                    and (
                                        grid[new_i][new_j] == 0
                                        or -level > grid[new_i][new_j]
                                    )
                                ):
                                    # print(new_i, new_j, grid[new_i][new_j], level)
                                    grid[new_i][new_j] = -level
                                    queue.appendleft((new_i, new_j))
        return -min((grid[i][j] for i in range(m) for j in range(n))) or -1

    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        level = 0
        while queue:
            queue_size = len(queue)
            level += 1
            for _ in range(queue_size):
                c_i, c_j = queue.pop()
                for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_i, new_j = c_i + delta_i, c_j + delta_j
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0:
                        # print(new_i, new_j, grid[new_i][new_j], level)
                        grid[new_i][new_j] = -level
                        queue.appendleft((new_i, new_j))
        return -min((grid[i][j] for i in range(m) for j in range(n))) or -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance(grid=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
    print(solution.maxDistance(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(
        solution.maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    )
