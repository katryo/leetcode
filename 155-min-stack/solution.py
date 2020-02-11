

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.cur_min = float('inf')

    def push(self, x: int) -> None:
        self.cur_min = min(x, self.cur_min)
        elem = (x, self.cur_min)
        self.stack.append(elem)

    def pop(self) -> None:
        if not self.stack:
            raise Error('No element')
        self.stack.pop()
        if self.stack:
            self.cur_min = self.stack[-1][1]
        else:
            self.cur_min = float('inf')

    def top(self) -> int:
        if not self.stack:
            raise Error('No element')
        top_elem = self.stack[-1]
        return top_elem[0]

    def getMin(self) -> int:
        if not self.stack:
            raise Error('No element')
        return self.cur_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
