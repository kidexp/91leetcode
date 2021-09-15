from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        index = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                count = 1
                index += 1
            elif count == 1:
                nums[index] = nums[i]
                count += 1
                index += 1
        return index


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
