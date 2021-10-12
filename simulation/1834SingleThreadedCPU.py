from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_with_index = []
        for i, task in enumerate(tasks):
            tasks_with_index.append((task[0], task[1], i))
        tasks_with_index.sort()
        result = [tasks_with_index[0][-1]]
        i, end_time = 1, tasks_with_index[0][0] + tasks_with_index[0][1]
        heap = []
        while i <= len(tasks_with_index):
            if i < len(tasks_with_index) and tasks_with_index[i][0] <= end_time:
                # find a task can be added into heap
                heapq.heappush(
                    heap,
                    (
                        tasks_with_index[i][1],
                        tasks_with_index[i][-1],
                        tasks_with_index[i][0],
                    ),
                )
                i += 1
            elif heap:
                # no task can be added to heap, but we can handle heap
                next_task = heapq.heappop(heap)
                end_time += next_task[0]
                result.append(next_task[1])
            elif i < len(tasks_with_index):
                # we need cpu idle for some time to add new task
                result.append(tasks_with_index[i][-1])
                end_time = tasks_with_index[i][0] + tasks_with_index[i][1]
                i += 1
            else:
                break

        return result

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_with_index = []
        for i, task in enumerate(tasks):
            tasks_with_index.append((task[0], task[1], i))
        tasks_with_index.sort()
        result = []
        heap = []
        end_time = 0
        for i in range(len(tasks_with_index)):
            while end_time < tasks_with_index[i][0] and heap:
                next_task = heapq.heappop(heap)
                end_time += next_task[0]
                result.append(next_task[1])
            if tasks_with_index[i][0] <= end_time:
                heapq.heappush(
                    heap,
                    (
                        tasks_with_index[i][1],
                        tasks_with_index[i][-1],
                        tasks_with_index[i][0],
                    ),
                )
            else:
                result.append(tasks_with_index[i][-1])
                end_time = tasks_with_index[i][0] + tasks_with_index[i][1]
        while heap:
            next_task = heapq.heappop(heap)
            end_time += next_task[0]
            result.append(next_task[1])
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]))
    print(solution.getOrder(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))
    print(
        solution.getOrder(
            tasks=[
                [19, 13],
                [16, 9],
                [21, 10],
                [32, 25],
                [37, 4],
                [49, 24],
                [2, 15],
                [38, 41],
                [37, 34],
                [33, 6],
                [45, 4],
                [18, 18],
                [46, 39],
                [12, 24],
            ]
        )
    )
