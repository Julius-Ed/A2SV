from typing import List
from bisect import bisect_left, bisect_right


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.votesAtT = {}
        self.totalVotes = {}

        for time, person in zip(time, persons):

            # increase total vote count of given person.
            if person not in self.totalVotes:
                self.totalVotes[person] = 1
            else:
                self.totalVotes[person] += 1

            if time not in self.votesAtT:
                self.votesAtT[time] = [(self.totalVotes[person], person)]

            elif self.votesAtT[time][-1][0] <= self.totalVotes[person]:
                self.votesAtT[time].append((self.totalVotes[person], person))

    def q(self, t):
        pass


persons = [0, 1, 1, 0, 0, 1, 0]
times = [0, 5, 10, 10, 15, 20, 25, 30]


Sol = TopVotedCandidate(persons, times)

for val in [3], [12], [25], [15], [24], [8]:
    print(Sol.q(val))
