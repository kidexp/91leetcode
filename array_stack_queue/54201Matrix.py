from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[-1] * n for _ in range(m)]
        queue = deque()
        visited_set = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.appendleft((i, j))
                    visited_set.add((i, j))
        level = 0
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                i, j = queue.pop()
                result[i][j] = level
                for delta_i, delta_j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    new_i, new_j = i + delta_i, j + delta_j
                    if (
                        0 <= new_i < m
                        and 0 <= new_j < n
                        and (new_i, new_j) not in visited_set
                    ):
                        visited_set.add((new_i, new_j))
                        queue.appendleft((new_i, new_j))
            level += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(solution.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
