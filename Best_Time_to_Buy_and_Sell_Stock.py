class Solution:
    def maxProfit(self, prices) -> int:

        maxPayoff = 0
        priceStack = []
        
        for priceIndex, price in enumerate(prices):

            if len(priceStack) == 0:
                priceStack.append(price)
                continue
            
            if price > priceStack[-1]:
                priceStack.append(price)
            
            if price <  priceStack[0]:
                priceStack = [price]
            
            if priceStack[-1] - priceStack[0] > maxPayoff:
                maxPayoff = priceStack[-1] - priceStack[0]
        
        return maxPayoff
                
            


Sol = Solution()


#prices = [7,1,5,3,6,4] # -> 5
#prices = [7,6,4,3,1] # -> 0
#prices = [1, 2, 3, 4, 10] # -> 9
prices = [0, 0, 0, 0, 0, 0]
print(Sol.maxProfit(prices))