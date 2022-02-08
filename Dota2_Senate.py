from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        queueR = deque([])
        queueD = deque([])

        for indexSenator, senator in enumerate(senate):
            if senator == "R":
                queueR.append(indexSenator)
            else:
                queueD.append(indexSenator)

        while len(queueR) > 0 and len(queueD) > 0:
            if queueR[0] < queueD[0]:

                queueR.append(max(queueD[-1], queueR[-1]) + 1)
                queueR.popleft()
                queueD.popleft()
            else:
                queueD.append(max(queueD[-1], queueR[-1]) + 1)

                queueD.popleft()
                queueR.popleft()

        if len(queueR) > 0:
            return "Radiant"
        else:
            return "Dire"
