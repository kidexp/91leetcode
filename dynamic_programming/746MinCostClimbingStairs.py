from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        dp = [0, 0, 0]
        for i in range(2, len(cost) + 1):
            dp[i % 3] = min(
                dp[(i - 1) % 3] + cost[i - 1], dp[(i - 2) % 3] + cost[i - 2]
            )
        return dp[len(cost) % 3]


if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
