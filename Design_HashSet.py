
class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.hashLength = 997
        self.hashvals = []

        for _ in range(self.hashLength):
            self.hashvals.append(Node("start"))

    def add(self, key: int) -> None:

        index = key % self.hashLength
        prev = None
        current = self.hashvals[index]

        while current:
            if current.val == key:
                return

            prev = current
            current = current.next
        prev.next = Node(key)

    def remove(self, key: int) -> None:

        index = key % self.hashLength

        prev = None
        current = self.hashvals[index]

        while current:

            if current.val == key:

                if current.next == None:
                    prev.next = None
                else:
                    prev.next = current.next

            prev = current
            current = current.next

    def contains(self, key: int) -> bool:

        index = key % self.hashLength

        current = self.hashvals[index]

        while current:
            if current.val == key:
                return True

            current = current.next

        return False


Sol = MyHashSet()
Sol.add(1)
Sol.add(2)
Sol.add(3)
Sol.add(2)
Sol.remove(2)
Sol.add(3)
print(Sol.contains(2))
