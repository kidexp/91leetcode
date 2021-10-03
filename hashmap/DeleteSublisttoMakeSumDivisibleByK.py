class Solution:
    def solve(self, nums, k):
        sum_ = sum(nums) % k
        if sum_ == 0:
            return 0
        sum_map = {0: -1}
        prefix_sum = 0
        min_length = None
        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_sum_mod = prefix_sum % k

            mod_diff = prefix_sum_mod - sum_
            if mod_diff < 0:
                mod_diff += k

            if mod_diff in sum_map:
                min_length = (
                    i - sum_map[mod_diff]
                    if min_length is None
                    else min(min_length, i - sum_map[mod_diff])
                )
                print(sum_map, prefix_sum_mod, mod_diff)

            sum_map[prefix_sum_mod] = i
        return -1 if min_length is None or min_length == len(nums) else min_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([1, 8, 6, 4, 5], 7))
    print(solution.solve([1, 8, 5], 7))
    print(solution.solve([2, 8, 5], 7))
    print(solution.solve([2, 8, 10], 7))
    print(solution.solve([2, 8, 7], 7))
    print(solution.solve([1,2], 2))
