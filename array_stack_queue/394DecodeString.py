class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                stack.append(int(s[i:j]))
                i = j - 1
            elif s[i] == "]":
                temp_str = ""
                while stack and stack[-1] != "[":
                    temp_str = stack.pop() + temp_str
                if stack and stack[-1] == "[":
                    stack.pop()
                if stack and type(stack[-1]) is int:
                    repeat_num = stack.pop()
                    stack.append(temp_str * repeat_num)
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)

    def decodeString(self, s: str) -> str:
        """
        simplified version
        """
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i].isdigit():
                if stack and type(stack[-1]) is int:
                    stack[-1] = stack[-1] * 10 + int(s[i])
                else:
                    stack.append(int(s[i]))
            elif s[i] == "]":
                temp_str = ""
                while stack and stack[-1] != "[":
                    temp_str = stack.pop() + temp_str
                if stack and stack[-1] == "[":
                    stack.pop()
                if stack and type(stack[-1]) is int:
                    repeat_num = stack.pop()
                    stack.append(temp_str * repeat_num)
            else:
                stack.append(s[i])
        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
    print(solution.decodeString("abc3[cd]xyz"))
