
class MinStack:

    def __init__(self):
        self.myMinStack = []


    def push(self, val: int) -> None:
        if len(self.myMinStack) == 0:
            self.myMinStack.append([val, val])
        else:

            currentMin = self.getMin()
        
            if val < currentMin:
                currentMin = val
            
            self.myMinStack.append([val, currentMin])
        
        
    def pop(self) -> None:
        self.myMinStack.pop()
 

    def top(self) -> int:
        if len(self.myMinStack) > 0:
            return self.myMinStack[-1][0]
        

    def getMin(self) -> int:
        if len(self.myMinStack) == 0:
            return None
        
        return self.myMinStack[-1][1]

    def printCompleteStack(self):
        for idnex in range(len(self.myMinStack) -1, -1, -1):
            print(self.myMinStack[idnex])
        

Sol = MinStack()
Sol.printCompleteStack()
print(Sol.push(2147483646))
Sol.printCompleteStack()
print(Sol.push(2147483646))
Sol.printCompleteStack()
print(Sol.push(2147483647))
Sol.printCompleteStack()
print(Sol.top())
Sol.printCompleteStack()
print(Sol.pop())
Sol.printCompleteStack()
print(Sol.getMin())
Sol.printCompleteStack()
print(Sol.pop())
Sol.printCompleteStack()
print(Sol.getMin())
Sol.printCompleteStack()
print(Sol.pop())
Sol.printCompleteStack()
print(Sol.push(2147483647))
Sol.printCompleteStack()
print(Sol.top())
Sol.printCompleteStack()
print(Sol.getMin())
Sol.printCompleteStack()
print(Sol.push(-2147483648))
Sol.printCompleteStack()
print(Sol.top())
Sol.printCompleteStack()
print(Sol.getMin())
Sol.printCompleteStack()
print(Sol.pop())
Sol.printCompleteStack()
print(Sol.getMin())
Sol.printCompleteStack()






"""
Input:
["MinStack","push","push","push",          "top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
Output:
[null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
Expected:
[null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]
"""