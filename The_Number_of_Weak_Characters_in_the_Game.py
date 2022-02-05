from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # sort in increasing order by first element (attack attribute), if equal, sort in decreasing order by second element (defense attribute).
        properties = sorted(properties, key=lambda x: (x[0], -x[1]))
        characterStack = [properties[0]]

        weakCardsCounter = 0

        for propertyIndex in range(1, len(properties)):

            # add to stack until top of stack is strictly smaller than new element.
            newAttackValue, newDefenseValue = properties[propertyIndex]
            currentAttackValue, currentDefenseValue = characterStack[-1]

            while characterStack and newAttackValue > currentAttackValue and newDefenseValue > currentDefenseValue:
                characterStack.pop()
                weakCardsCounter += 1

                if characterStack:
                    currentAttackValue, currentDefenseValue = characterStack[-1]

            characterStack.append(properties[propertyIndex])

        return weakCardsCounter


Sol = Solution()
print(Sol.numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0)
print(Sol.numberOfWeakCharacters([[2, 2], [3, 3]]) == 1)
print(Sol.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]) == 1)
