class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        removeStack = []
        toBeRemoved = []

        for index, char in enumerate(s):

            if char != "(" and char != ")":
                continue

            if len(removeStack) == 0 and char == ")":
                toBeRemoved.append(index)
                continue

            if char == "(":
                removeStack.append(index)

            elif char == ")":
                removeStack.pop()

        toBeRemoved += removeStack
        toBeRemoved = set(toBeRemoved)

        res = ""

        for index, char in enumerate(s):
            if index not in toBeRemoved:
                res += char

        return res


Sol = Solution()
s = "lee(t(c)o)de)"
print(Sol.minRemoveToMakeValid(s))
