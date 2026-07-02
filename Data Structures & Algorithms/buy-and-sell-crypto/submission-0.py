class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestprofit = 0

        for i, num in enumerate(prices):

            peakprice = max(prices[i : len(prices)]) 
            profit = peakprice - num
            bestprofit = max(profit, bestprofit)
        
        return bestprofit