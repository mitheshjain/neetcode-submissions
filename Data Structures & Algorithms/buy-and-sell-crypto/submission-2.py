class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        b,s=0,1
        maxProfit=0
        while s<len(prices):
            maxProfit=max(maxProfit,prices[s]-prices[b])

            if prices[b]> prices[s]:
                b=s
            s+=1
        
        return maxProfit

        