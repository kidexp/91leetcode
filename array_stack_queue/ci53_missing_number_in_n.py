from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number= 0
        for i in range(len(nums)+1):
            if i < len(nums):
                missing_number ^= nums[i]
            missing_number ^= i
        return missing_number

solution = Solution()
print(solution.missingNumber([0,1,3]))
print(solution.missingNumber([0,1,2,3,4,5,6,7,9]))