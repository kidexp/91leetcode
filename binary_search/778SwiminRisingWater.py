from typing import List
from collections import deque


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def bfs(t):
            queue = deque([(0, 0)])
            visited_node = set((0, 0))
            while queue:
                queue_length = len(queue)
                for _ in range(queue_length):
                    i, j = queue.pop()
                    if (i, j) == (n - 1, n - 1):
                        return True
                    for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_i, new_j = i + delta_i, j + delta_j
                        if (
                            0 <= new_i < n
                            and 0 <= new_j < n
                            and (new_i, new_j) not in visited_node
                            and grid[new_i][new_j] <= t
                        ):
                            queue.appendleft((new_i, new_j))
                            visited_node.add((new_i, new_j))
            return False

        start, end = grid[0][0], max((max(grid[i]) for i in range(n)))
        while start <= end:
            mid = (start + end) // 2
            if bfs(mid):
                end = mid - 1
            else:
                start = mid + 1

        return start


if __name__ == "__main__":
    solution = Solution()
    print(solution.swimInWater(grid=[[0]]))
    print(solution.swimInWater(grid=[[0, 2], [1, 3]]))
    print(
        solution.swimInWater(
            grid=[
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
    )
