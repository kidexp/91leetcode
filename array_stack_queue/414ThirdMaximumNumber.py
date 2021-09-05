from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_large, second_large, third_large = None, None, None
        for num in nums:
            if num in [first_large, second_large, third_large]:
                continue
            elif first_large is None or num > first_large:
                first_large, second_large, third_large = num, first_large, second_large
            elif second_large is None or num > second_large:
                second_large, third_large = num, second_large
            elif third_large is None or num > third_large:
                third_large = num
        return third_large if third_large is not None else first_large


if __name__ == "__main__":
    solution = Solution()
    print(solution.thirdMax([3, 2, 1]))
    print(solution.thirdMax([1, 2]))
    print(solution.thirdMax([2, 2, 1, 3]))
