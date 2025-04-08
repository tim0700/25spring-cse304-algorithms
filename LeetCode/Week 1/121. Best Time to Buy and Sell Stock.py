'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?source=submission-ac
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # your code
        maxProfit = 0
        lowPrice = prices[0]
        for i in range (1, len(prices)):
            if prices[i] < lowPrice:
                lowPrice = prices[i]
            if prices[i] - lowPrice > maxProfit:
                maxProfit = prices[i] - lowPrice

        return maxProfit 