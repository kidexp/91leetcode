from typing import List
from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for start, end in dislikes:
            graph[start].append(end)
            graph[end].append(start)

        def dfs(node, color):
            if node in node_color:
                if node_color[node] != color:
                    return False
                return True
            node_color[node] = color
            return (
                all(dfs(next_node, not color) for next_node in graph[node])
                if graph[node]
                else True
            )

        node_color = {}
        for node in range(1, n + 1):
            if node not in node_color:
                if not dfs(node, True):
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]]))
    print(solution.possibleBipartition(n=3, dislikes=[[1, 2], [1, 3], [2, 3]]))
    print(
        solution.possibleBipartition(
            n=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        )
    )

print(
    solution.possibleBipartition(
        n=6, dislikes=[[6, 2], [1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    )
)
