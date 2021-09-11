from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_index_dict = defaultdict(list)
        for i, num in enumerate(nums):
            num_index_dict[num].append(i)
        max_frequency = 0
        shortest_length = None
        for num in num_index_dict:
            if len(num_index_dict[num]) >= max_frequency:
                if (
                    len(num_index_dict[num]) > max_frequency
                    or (num_index_dict[num][-1] - num_index_dict[num][0] + 1)
                    < shortest_length
                ):
                    shortest_length = (
                        num_index_dict[num][-1] - num_index_dict[num][0] + 1
                    )
                max_frequency = len(num_index_dict[num])
        return shortest_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.findShortestSubArray(nums=[1, 2, 2, 3, 1]))
    print(solution.findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2]))
