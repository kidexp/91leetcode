from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast


if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicate([1, 3, 4, 2, 2]))
    print(solution.findDuplicate([3, 1, 3, 4, 2]))
    print(solution.findDuplicate([1, 1]))
    print(solution.findDuplicate([1, 1, 2]))
    print(solution.findDuplicate([2, 2, 2]))
