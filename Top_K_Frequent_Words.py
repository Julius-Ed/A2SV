from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        wordToFreq = Counter(words)

        maxHeap = []

        for word in wordToFreq:
            maxHeap.append([wordToFreq[word] * (-1), word])

        heapq.heapify(maxHeap)

        res = []

        while len(res) < k:
            res.append(heapq.heappop(maxHeap)[1])

        return res


Sol = Solution()
print(Sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
