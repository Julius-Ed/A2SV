# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:

            mid = (left + right) // 2

            if isBadVersion(mid) == True:
                right = mid

            elif isBadVersion(mid) == False:
                left = mid + 1

        return int(right)
    
def isBadVersion():
    pass


Sol = Solution()
Sol.firstBadVersion()

 