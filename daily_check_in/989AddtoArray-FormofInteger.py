from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        m = 0
        for digit in num:
            m = m * 10 + digit
        sum_ = m + k
        result = []
        while sum_:
            result.append(sum_ % 10)
            sum_ //= 10
        return result[::-1] if result else [0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.addToArrayForm(num=[1, 2, 0, 0], k=34))
    print(solution.addToArrayForm(num=[2, 7, 4], k=181))
    print(solution.addToArrayForm(num=[2, 1, 5], k=806))
    print(solution.addToArrayForm(num=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], k=1))
    print(solution.addToArrayForm(num=[0], k=0))
