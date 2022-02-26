from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
         
        lookUps = [   
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"]]

        roman = ""

        index = 0
        while index < len(lookUps):
            lookup = lookUps[index]

            if lookup[0] <= num:
                roman = roman + lookup[1]
                num -= lookup[0]

                index = 0
                if num == 0:
                    return roman
        
            else:
                index += 1
        
        return roman

Sol = Solution()
print(Sol.intToRoman(58))
print(Sol.intToRoman(1994))
print(Sol.intToRoman(2000))