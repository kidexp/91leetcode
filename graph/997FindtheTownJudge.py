from typing import List

from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for node1, node2 in trust:
            out_degree[node1] += 1
            in_degree[node2] += 1
        for node in in_degree:
            if in_degree[node] == n - 1 and out_degree[node] == 0:
                return node
        return -1 if n > 1 else 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findJudge(n=2, trust=[[1, 2]]))
    print(solution.findJudge(n=3, trust=[[1, 3], [2, 3]]))
    print(solution.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
    print(solution.findJudge(n=3, trust=[[1, 2], [2, 3]]))
    print(solution.findJudge(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
