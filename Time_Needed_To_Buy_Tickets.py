from typing import List
from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ticketsqueue = deque(tickets)
        targetPersonTickets = k

        secondsCounter = 0
        while ticketsqueue[targetPersonTickets] > 0:

            secondsCounter += 1

            ticketsLeftToBuy = ticketsqueue.popleft() - 1

            if targetPersonTickets == 0 and ticketsLeftToBuy == 0:
                return secondsCounter

            if ticketsLeftToBuy > 0:
                ticketsqueue.append(ticketsLeftToBuy)

            if targetPersonTickets == 0:
                targetPersonTickets = len(ticketsqueue) - 1
            else:
                targetPersonTickets -= 1

        return secondsCounter


Sol = Solution()
print(Sol.timeRequiredToBuy([2, 3, 2], 2) == 6)
print(Sol.timeRequiredToBuy([5, 1, 1, 1], 0) == 8)
print(Sol.timeRequiredToBuy([100], 0) == 100)
