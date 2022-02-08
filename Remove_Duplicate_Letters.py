from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occurenceDictionary = Counter(s)
        myStack = []

        for character in s:
            
            occurenceDictionary[character] -= 1
            if character in myStack:
                continue
            
            while myStack and myStack[-1] > character and occurenceDictionary[myStack[-1]]:
                myStack.pop()
            
            myStack.append(character)

        return "".join(myStack)


Sol = Solution()
print(Sol.removeDuplicateLetters("cbacdcbc") == "acdb")
print(Sol.removeDuplicateLetters("bcabc") == "abc")
print(Sol.removeDuplicateLetters("ecbacba") == "eacb")