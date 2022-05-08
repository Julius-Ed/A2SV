class Logger:

    def __init__(self):
        self.printedMessages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.printedMessages:
            self.printedMessages[message] = timestamp
            return True

        elif timestamp - self.printedMessages[message] >= 10:
            self.printedMessages[message] = timestamp
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

Sol = Logger()

arr = [[1, "foo"], [2, "bar"], [3, "foo"],
       [8, "bar"], [10, "foo"], [11, "foo"]]


for timestamp, message in arr:
    print(Sol.shouldPrintMessage(timestamp, message))
