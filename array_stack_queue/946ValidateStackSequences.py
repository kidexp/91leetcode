from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        verbose
        """
        i = j = 0
        stack = []
        while j < len(popped):
            while i < len(pushed) and pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            if i == len(pushed):
                return False
            else:
                stack.append(pushed[i])
                i += 1
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        simplify
        """
        j = 0
        stack = []
        for item in pushed:
            stack.append(item)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
    )
    print(
        solution.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])
    )
