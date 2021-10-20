class Solution:
    def solve(self, nums):
        nums.sort()
        start, end = 0, (nums[-1] - nums[0])/3

        def can_cover(redis):
            start = nums[0]
            count = 1
            for num in nums:
                if start + 2 * redis < num:
                    start = num
                    count += 1
                    if count > 3:
                        return False
            return True

        while (end - start) > 0.000001:
            print(start, end)
            mid = (start + end) / 2
            if can_cover(mid):
                end = mid
            else:
                start = mid
        return start


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([3, 4, 5, 6]))
