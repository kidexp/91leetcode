from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        single_solution = []

        def dfs(i):
            if i == 0:
                result.append(int("".join((str(digit) for digit in single_solution))))
                return
            for digit in range(10):
                if i == n:
                    if digit == 0:
                        continue
                if (
                    not single_solution
                    or (single_solution[-1] - digit == k)
                    or (digit - single_solution[-1] == k)
                ):
                    single_solution.append(digit)
                    dfs(i - 1)
                    single_solution.pop()

        dfs(n)
        return result

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        single_solution = []

        def dfs(digit):
            single_solution.append(digit)
            if len(single_solution) < n:
                if 10 > digit + k >= 0:
                    dfs(digit + k)
                if k > 0 and 10 > digit - k >= 0:
                    dfs(digit - k)
            if len(single_solution) == n:
                result.append(int("".join((str(item) for item in single_solution))))
            single_solution.pop()

        for i in range(1, 10):
            dfs(i)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.numsSameConsecDiff(n=3, k=7))
    print(solution.numsSameConsecDiff(n=2, k=1))
    print(solution.numsSameConsecDiff(n=2, k=0))
    print(solution.numsSameConsecDiff(n=2, k=2))
