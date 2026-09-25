class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buyPrice=prices[0]
        for p in prices:
            if p<buyPrice:
                buyPrice=p
            else:
                profit=max(profit,p-buyPrice)

        return profit        