from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        point_distance_dict = {i: defaultdict(int) for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                distance = (points[i][0] - points[j][0]) ** 2 + (
                    points[i][1] - points[j][1]
                ) ** 2
                point_distance_dict[i][distance] += 1
                point_distance_dict[j][distance] += 1
        result = 0
        for i in range(n):
            for distance in point_distance_dict[i]:
                if point_distance_dict[i][distance] > 1:
                    result += point_distance_dict[i][distance] * (
                        point_distance_dict[i][distance] - 1
                    )
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfBoomerangs(points=[[0, 0], [1, 0], [2, 0]]))
    print(solution.numberOfBoomerangs(points=[[1, 1], [2, 2], [3, 3]]))
    print(solution.numberOfBoomerangs(points=[[1, 1]]))
