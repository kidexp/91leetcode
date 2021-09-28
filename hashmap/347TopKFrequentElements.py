from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        heap solution
        """
        num_count_dict = Counter(nums)
        num_count_heap = [(-count, num) for num, count in num_count_dict.items()]
        heapq.heapify(num_count_heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(num_count_heap)[1])
        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        bucket sort
        """
        num_count_dict = Counter(nums)
        num_bucket = [[] for _ in range(len(nums))]
        for num, count in num_count_dict.items():
            num_bucket[count - 1].append(num)
        result = []
        for i in range(len(num_bucket) - 1, -1, -1):
            if num_bucket[i]:
                result.extend(num_bucket[i])
            if len(result) == k:
                break
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    print(solution.topKFrequent(nums=[1], k=1))
