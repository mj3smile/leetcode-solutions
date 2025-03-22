class MyQueue:
    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        i = 0
        while i < len(self.stack) - 1:
            self.stack[i], self.stack[i + 1] = self.stack[i + 1], self.stack[i]
            i += 1
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()