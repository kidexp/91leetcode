from typing import List

from sortedcontainers import SortedList


class Solution:
    def solve(self, nums: List[int]):
        d = SortedList()
        ans = 0

        for num in nums:
            i = d.bisect_right(num * 3)
            ans += len(d) - i
            d.add(num)
        return ans

    def solve(self, nums: List[int]):
        triple_count = 0

        def merge(start, mid, end):
            nonlocal triple_count
            i, j, temp = start, mid + 1, []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            ti, tj = start, mid + 1
            while ti <= mid and tj <= end:
                if nums[ti] <= 3 * nums[tj]:
                    ti += 1
                else:
                    triple_count += mid - ti + 1
                    tj += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            for i in range(len(temp)):
                nums[start + i] = temp[i]

        def merge_sort(start, end):
            if start >= end:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid + 1, end)
            merge(start, mid, end)

        merge_sort(0, len(nums) - 1)
        return triple_count


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([]))
    print(
        solution.solve(
            [
                1,
            ]
        )
    )
    print(solution.solve([1, 2]))
    print(
        solution.solve(
            [
                5,
                1,
                2,
            ]
        )
    )
    print(
        solution.solve(
            [
                5,
                7,
                1,
                2,
            ]
        )
    )
    print(solution.solve([7, 1, 2]))
