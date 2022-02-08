
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.queue.insert((len(self.queue) // 2), val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return -1

    def popMiddle(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(((len(self.queue) - 1) // 2))
        else:
            return -1

    def popBack(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return -1
