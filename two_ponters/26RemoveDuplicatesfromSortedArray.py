from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = -1
        for i, num in enumerate(nums):
            if start == -1 or nums[start] != num:
                start += 1
                nums[start] = num
        return start + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([]))
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 3, 3, 4]))
