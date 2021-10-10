class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal_move = 0
        vertical_move = 0
        for char in moves:
            if char == "U":
                vertical_move += 1
            elif char == "D":
                vertical_move -= 1
            elif char == "L":
                horizontal_move += 1
            else:
                horizontal_move -= 1
        return horizontal_move == 0 and vertical_move == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.judgeCircle("UD"))
    print(solution.judgeCircle("LL"))
    print(solution.judgeCircle("RRDD"))
    print(solution.judgeCircle("LDRRLRUULR"))
