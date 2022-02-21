from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        occ = Counter(s)
        req = {}
        res = len(s)

        for char in occ:
            if occ[char] > len(s) // 4:
                req[char] = occ[char] - len(s) // 4

        if len(req) == 0:
            return 0

        window = {}
        left = 0

        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            if self.checkBalance(req, window):
                res = min(res, right - left + 1)

                while left < right:

                    if window[s[left]] <= 1:
                        window.pop(s[left])
                    else:
                        window[s[left]] -= 1

                    left += 1

                    if self.checkBalance(req, window):
                        res = min(res, right - left + 1)

        return res

    def checkBalance(self, req, window) -> bool:

        for char in req:
            if not (char in window and window[char] >= req[char]):
                return False

        return True


Sol = Solution()
print(Sol.balancedString("WQWRQQQW") == 3)
print(Sol.balancedString("QWER") == 0)
print(Sol.balancedString("QQWE") == 1)
print(Sol.balancedString("QQQW") == 2)


print(Sol.balancedString("WQWRQEQQWERQWWWEREWRQQWWWWQW") == 6)
