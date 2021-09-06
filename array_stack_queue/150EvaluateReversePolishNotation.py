from typing import List


def compute(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    return int(num1 / num2)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        from end to begin
        """
        stack = []
        index = len(tokens) - 1

        while index >= 0:
            item = tokens[index]
            if item.lstrip("-").isnumeric():
                current_num = int(item)
                while stack and type(stack[-1]) is int:
                    next_num = stack.pop()
                    operator = stack.pop()
                    current_num = compute(current_num, next_num, operator)
                stack.append(current_num)
            else:
                stack.append(item)
            index -= 1

        return stack[-1]

    def evalRPN(self, tokens: List[str]) -> int:
        """
        from begin to end
        """

        stack = []
        for item in tokens:
            if item not in "+-*/":
                stack.append(int(item))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(compute(num1, num2, item))
        return stack[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))
    print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(
        solution.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
