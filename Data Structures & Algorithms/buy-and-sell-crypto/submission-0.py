class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i<j and prices[i] < prices[j]:
                    res = max(res, prices[j] - prices[i])
        return res