class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        maxProfit=0
        for p in prices:
            if p <min:
                min=p
            else:
                maxProfit=max(maxProfit,p-min)
        
        return maxProfit