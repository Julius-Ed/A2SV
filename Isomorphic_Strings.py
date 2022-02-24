
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapStoT = {}
        mapTtoS = {}

        for charS, charT in zip(s, t):

            if charS not in mapStoT and charT not in mapTtoS:
                mapStoT[charS] = charT
                mapTtoS[charT] = charS

            elif charS in mapStoT and charT != mapStoT[charS] or charT in mapTtoS and charS != mapTtoS[charT]:
                return False

        return True


Sol = Solution()
print(Sol.isIsomorphic("bbbaaaba", "aaabbbba") == False)
print(Sol.isIsomorphic("badc", "baba") == False)
