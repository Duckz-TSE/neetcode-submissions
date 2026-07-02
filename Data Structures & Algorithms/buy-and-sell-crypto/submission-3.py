class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestprofit = 0
        bestpricetobuy = prices[0]

        for num in prices:
            bestpricetobuy = min(bestpricetobuy,num)
            profit = num - bestpricetobuy
            bestprofit = max(bestprofit,profit)
            
        return bestprofit