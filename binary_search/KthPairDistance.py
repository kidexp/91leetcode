class Solution:
    def solve(self, nums, k):
        nums.sort()

        def count_diff_pair_order(diff):
            start = pair_order = 0
            for i in range(1, len(nums)):
                while nums[i] - nums[start] > diff:
                    start += 1
                pair_order += i - start
            print("pair", diff, pair_order)
            return pair_order

        start, end = 0, nums[-1] - nums[0]
        while start <= end:
            print(start, end)
            mid = (start + end) // 2
            if count_diff_pair_order(mid) >= k + 1:
                end = mid - 1
            else:
                start = mid + 1
        return start


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(nums=[1, 5, 3, 2], k=3))
    print(solution.solve(nums=[1, 5, 3, 2], k=4))
