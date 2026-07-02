class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestprofit = 0
        bestpricetobuy = prices[0]
        max(prices)

        for i, num in enumerate(prices):
            bestpricetobuy = min(bestpricetobuy,num)
            profit = num - bestpricetobuy
            bestprofit = max(bestprofit,profit)
            
        return bestprofit