
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        wordLength = 0
        for symbol in s:
            if symbol.isdigit():
                wordLength *= int(symbol)
            else:
                wordLength += 1

        for symbolIndex in range(len(s) - 1, -1, -1):
            if symbolIndex == (k - 1):
                return s[symbolIndex]
            
            if s[symbolIndex].isdigit():
                k = k % wordLength
                wordLength = wordLength / int(s[symbolIndex])
            else:
                wordLength -= 1


    
Sol = Solution()

print(Sol.decodeAtIndex("leet2code3", k = 10))

