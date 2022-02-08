class MyCircularDeque:

    def __init__(self, k: int):
        self.dequeu = []
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if len(self.dequeu) < self.maxSize:
            self.dequeu = [value] + self.dequeu
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.dequeu) < self.maxSize:
            self.dequeu += [value]
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.dequeu) > 0:
            self.dequeu = self.dequeu[1:]
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.dequeu) > 0:
            self.dequeu.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.dequeu) > 0:
            return self.dequeu[0]
        return -1

    def getRear(self) -> int:
        if len(self.dequeu) > 0:
            return self.dequeu[-1]
        return -1

    def isEmpty(self) -> bool:
        if len(self.dequeu) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.dequeu) == self.maxSize:
            return True
        return False

    def printQueue(self):
        print(self.dequeu)


Sol = MyCircularDeque(5)
Sol.insertFront(3)
Sol.insertFront(2)
print(Sol.insertFront(1))
print(Sol.insertFront(0))
print(Sol.insertLast(4))
Sol.printQueue()
print(Sol.deleteFront())
Sol.printQueue()
print(Sol.deleteLast())
Sol.printQueue()
print(Sol.getFront())

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
