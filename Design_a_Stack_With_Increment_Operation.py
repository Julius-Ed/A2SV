class CustomStack:

    def __init__(self, maxSize: int):
        
        self.myStack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        
        if len(self.myStack) < self.maxSize:
            self.myStack.append(x)
        

    def pop(self) -> int:
        if len(self.myStack) == 0:
            return -1
        return self.myStack.pop()
   
    def increment(self, k: int, val: int) -> None:
        
        if len(self.myStack) < k:
            k = len(self.myStack)
        
        for stackIndex in range(0, k):
            self.myStack[stackIndex] = self.myStack[stackIndex] + val