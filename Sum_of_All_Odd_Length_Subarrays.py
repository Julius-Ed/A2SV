from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        acc = 0
        for index, value in enumerate(arr):

            acc += (((index + 1) * (len(arr) - index) + 1) // 2) * value
        
        return acc

    def sumOddLengthSubarraysSol(self, A):
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) / 2 * a
        return res


Sol = Solution()
print(Sol.sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58)
print(Sol.sumOddLengthSubarrays([1, 2]) == 3)

print(Sol.sumOddLengthSubarrays([10, 11, 12]) == 66)

