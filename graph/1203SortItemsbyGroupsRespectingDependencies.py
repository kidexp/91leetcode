from typing import List
from collections import deque, defaultdict


def topological_sort(node_list, in_degree_dict, graph):
    result = []
    queue = deque()
    for node in node_list:
        if in_degree_dict[node] == 0:
            queue.append(node)
    while queue:
        node = queue.pop()
        result.append(node)
        for next_node in graph[node]:
            in_degree_dict[next_node] -= 1
            if in_degree_dict[next_node] == 0:
                queue.appendleft(next_node)
    return result


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        # assign unique group id for project without a group
        max_project = m
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = max_project
                max_project += 1
        distinct_group_list = list(set(group))
        # build group and project graph
        group_in_degree = defaultdict(int)
        group_graph = defaultdict(list)
        project_in_degree = defaultdict(int)
        project_graph = defaultdict(list)
        group_project_dict = defaultdict(list)
        for i in range(len(beforeItems)):
            group_project_dict[group[i]].append(i)
            for dep in beforeItems[i]:
                
                if group[i] != group[dep]:
                    group_in_degree[group[i]] += 1
                    group_graph[group[dep]].append(group[i])
                else:
                    project_in_degree[i] += 1
                    project_graph[dep].append(i)
        # sort the group first
        sorted_group = topological_sort(
            distinct_group_list, group_in_degree, group_graph
        )
        if len(sorted_group) != len(distinct_group_list):
            return []

        result = []
        # sort project in each group
        for i in sorted_group:
            sorted_projects = topological_sort(
                group_project_dict[i], project_in_degree, project_graph
            )
            if len(sorted_projects) != len(group_project_dict[i]):
                return []
            result.extend(sorted_projects)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.sortItems(
            n=8,
            m=2,
            group=[-1, -1, 1, 0, 0, 1, 0, -1],
            beforeItems=[[], [6], [5], [6], [3, 6], [], [], []],
        )
    )
    print(
        solution.sortItems(
            n=8,
            m=2,
            group=[-1, -1, 1, 0, 0, 1, 0, -1],
            beforeItems=[[], [6], [5], [6], [3], [], [4], []],
        )
    )
    print(
        solution.sortItems(
            n=5,
            m=5,
            group=[2, 0, -1, 3, 0],
            beforeItems=[[2, 1, 3], [2, 4], [], [], []],
        )
    )
