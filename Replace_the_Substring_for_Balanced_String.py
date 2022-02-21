
class Solution:
    def balancedString(self, s: str) -> int:

        charMap = [0] * 4
        targetWindow = [0] * 4
        currentWindow = [0] * 4
        res = float("inf")

        for c in s:
            charMap[self.charToInt(c)] += 1

        for index, val in enumerate(charMap):
            if val - len(s) // 4 > 0:
                targetWindow[index] = val - (len(s) // 4)

        if targetWindow == [0, 0, 0, 0]:
            return 0

        left, right = -1, 0

        while right < len(s):
            currentWindow[self.charToInt(s[right])] += 1

            while self.validateWindow(targetWindow, currentWindow) and left < right:
                res = min(res, right - left)
                left += 1
                currentWindow[self.charToInt(s[left])] -= 1
            
            right += 1
        
        return res

    def validateWindow(self, targetWindow, currentWindow):
        for valTarget, valCurrent in zip(targetWindow, currentWindow):
            if valCurrent < valTarget:
                return False

        return True

    def charToInt(self, c):
        if c == "Q":
            return 0
        if c == "W":
            return 1
        if c == "E":
            return 2
        if c == "R":
            return 3

Sol = Solution()
#print(Sol.balancedString("WQWRQQQW") == 3)
#print(Sol.balancedString("QWER") == 0)
#print(Sol.balancedString("QQWE") == 1)
#print(Sol.balancedString("QQQW") == 2)
#print(Sol.balancedString("WQWRQEQQWERQWWWEREWRQQWWWWQW") == 6)
