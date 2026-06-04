class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        if len(self.st2) == 0:
            self.st1.append(x)

        else:
            while len(self.st2) > 0:
                self.st1.append(self.st2.pop())

            self.st1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.st2.pop()

    def peek(self) -> int:
        while len(self.st1) > 0:
            self.st2.append(self.st1.pop())

        if len(self.st2) > 0:
            return self.st2[-1]
        else:
            return

    def empty(self) -> bool:
        return len(self.st1) == 0 and len(self.st2) == 0

        # Your MyQueue object will be instantiated and called as such:


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
