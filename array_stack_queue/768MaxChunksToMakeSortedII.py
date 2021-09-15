from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        monotonous non-decreasing stack
        """
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                max_value = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(max_value)
            else:
                stack.append(num)
        return len(stack)

    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        sorting and compare sum
        """
        count = 0
        sorted_array = sorted(arr)
        s1 = s2 = 0
        for num1, num2 in zip(arr, sorted_array):
            s1 += num1
            s2 += num2
            if s1 == s2:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxChunksToSorted([1, 2, 3, 4, 5]))
    print(solution.maxChunksToSorted([5, 4, 3, 2, 1]))
    print(solution.maxChunksToSorted([2, 1, 3, 4, 4]))
    print(solution.maxChunksToSorted([2, 3, 1, 4, 4]))
    print(solution.maxChunksToSorted([4, 2, 2, 1, 1]))
