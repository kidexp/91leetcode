from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if (
                0 < nums[i] <= len(nums)
                and (i + 1) != nums[i]
                and nums[nums[i] - 1] != nums[i]
            ):
                switch_index = nums[i] - 1
                nums[i], nums[switch_index] = nums[switch_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([1, 2, 0]))
    print(solution.firstMissingPositive([3, 4, -1, 1]))
    print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
    print(solution.firstMissingPositive([0, 1, 2, 1, 4]))
    print(solution.firstMissingPositive([0, 1, 2, 2, 4]))
    print(solution.firstMissingPositive([0, 1, 1]))
