class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        minVal, maxVal = 1, m*n

        def count(x):

            total = 0

            for i in range(1, m + 1):
                total += min(x//i, n)

            return total

        left, right, mid, ans = 0, m*n, 0, 0
        while left <= right:

            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right, ans = mid - 1, mid
        return ans
