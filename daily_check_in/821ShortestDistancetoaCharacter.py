from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = [i for i in range(len(s)) if s[i] == c]
        c_index = 0
        results = []
        for i in range(len(s)):
            if c_index < len(positions) - 1 and i == positions[c_index + 1]:
                c_index += 1
            if c_index == len(positions) - 1:
                results.append(abs(i - positions[c_index]))
            else:
                results.append(
                    min(abs(i - positions[c_index]), abs(positions[c_index + 1] - i))
                )
        return results


if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestToChar(s="loveleetcode", c="e"))
    print(solution.shortestToChar(s="aaab", c="b"))
    print(solution.shortestToChar(s="aaab", c="a"))
