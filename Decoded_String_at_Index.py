
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        size = 0

        for symbol in s:
            if symbol.isdigit():
                size *= int(symbol)
            else:
                size += 1

        for symbol in reversed(s):

            k = k % size

            if k == 0 and symbol.isalpha():
                return symbol

            if symbol.isdigit():
                size = size / int(symbol)

            else:
                size -= 1


Sol = Solution()

print(Sol.decodeAtIndex("leet2code3", k = 10))
print(Sol.decodeAtIndex("a2345678999999999999999", k = 1))
