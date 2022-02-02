
class Solution:
    def isValid(self, s: str) -> bool:
        
        matchingSymbolDict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stackOfSymbols = []

        for symbol in s:
            if symbol not in matchingSymbolDict:
                stackOfSymbols.append(symbol)
            elif stackOfSymbols and stackOfSymbols[-1] == matchingSymbolDict[symbol]:
                stackOfSymbols.pop()
            else:
                stackOfSymbols.append(symbol)
        
        if len(stackOfSymbols) == 0:
            return True
        else:
            return False



Sol = Solution()
print(Sol.isValid('([]))'))