from collections import deque, defaultdict


class Solution:
    def solve(self, graph, target):
        if not graph:
            return -1
        graph_dict = defaultdict(list)
        m = len(graph)
        for i in range(m):
            for j in graph[i]:
                graph_dict[i].append(j)
        queue = deque([target])
        visited_set = set()
        level = 0
        while queue:
            level += 1
            queue_size = len(queue)
            for _ in range(queue_size):
                node = queue.pop()
                for next_node in graph_dict[node]:
                    if next_node == target:
                        return level
                    elif next_node not in visited_set:
                        visited_set.add(next_node)
                        queue.appendleft(next_node)
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([[], [1]], 1))
    print(solution.solve([[1], [2], [0]], 0))
    print(
        solution.solve(
            [
                [1],
                [2],
                [4],
                [],
                [0],
            ],
            3,
        )
    )

    print(
        solution.solve(
            [
                [1],
                [2],
                [4],
                [0],
                [0],
            ],
            0,
        )
    )
    print(
        solution.solve(
            [
                [1],
                [2],
                [4],
                [3],
                [0],
            ],
            3,
        )
    )
