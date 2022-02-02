class MinStack:

    def __init__(self):
        self.myMinStack = []
        

    def push(self, val: int) -> None:
        self.myMinStack.append(val)
        

    def pop(self) -> None:
        self.myMinStack.pop()
        

    def top(self) -> int:
        if len(self.myMinStack) > 0:
            return self.myMinStack[-1]
        

    def getMin(self) -> int:
        if len(self.myMinStack) > 0:
            return min(self.myMinStack)

    def printCompleteStack(self):
        for idnex in range(len(self.myMinStack) -1, -1, -1):
            print(self.myMinStack[idnex])
        

Sol = MinStack()
Sol.push(-2)
Sol.push(0)
Sol.push(-3)
#Sol.printCompleteStack()

print(Sol.getMin())