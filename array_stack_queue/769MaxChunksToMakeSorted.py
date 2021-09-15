from typing import List


class Solution:
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

    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        use index
        """
        count = max_value = 0
        for i in range(len(arr)):
            max_value = max(max_value, arr[i])
            if max_value == i:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxChunksToSorted([4, 3, 2, 1, 0]))
    print(solution.maxChunksToSorted([1, 0, 2, 3, 4]))
    print(solution.maxChunksToSorted([1, 2, 0, 4, 3]))
