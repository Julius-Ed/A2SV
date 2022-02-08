from collections import deque

class RecentCounter:

    def __init__(self):
        self.request = deque()

    def ping(self, t: int) -> int:
        
        self.request.append(t)

        while len(self.request) > 0 and self.request[0] < t - 3000:
            self.request.popleft()

        return len(self.request)



recentCounter = RecentCounter()


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


recentCounter.ping(1)#;     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100)#;   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001)#;  // requests = [1, 100, 3001], range is [1,3001], return 3
print(recentCounter.ping(3002))#;  // requests = [1, 100, 3001, 3002], range is [2,3002], 


