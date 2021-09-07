class CustomStack:
    """
    O(n) increment
    """

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


class CustomStack:
    """
    O(1) increment
    """

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if self.stack:
            if len(self.stack) > 1:
                self.inc[-2] += self.inc[-1]
            return self.stack.pop() + self.inc.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.inc[min(k, len(self.stack)) - 1] += val


if __name__ == "__main__":
    customStack = CustomStack(3)
    customStack.push(1)
    customStack.push(2)
    print(customStack.pop())
    customStack.push(2)
    customStack.push(3)
    customStack.push(4)
    customStack.increment(5, 100)
    customStack.increment(2, 100)
    print(customStack.pop())
    print(customStack.pop())
    print(customStack.pop())
    print(customStack.pop())
