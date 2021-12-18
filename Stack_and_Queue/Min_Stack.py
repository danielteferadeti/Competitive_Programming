class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = []
        self.minStack = [sys.maxsize]
        
    def push(self, val: int) -> None:
        if val <= self.minStack[len(self.minStack)-1]:
            self.Stack.append(val)
            self.minStack.append(val)
        else:
            self.Stack.append(val)

    def pop(self) -> None:
        val = self.Stack.pop()
        if val==self.minStack[len(self.minStack)-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.Stack[len(self.Stack)-1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()