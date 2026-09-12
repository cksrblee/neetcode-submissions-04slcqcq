class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        l , r = 0 , 1 
        profit = 0
        for i in range(len(prices)):
            if prices[l] > prices[i]:
                l = i
            
            if prices[r] < prices[i]:
                r = i
            
            if l >= r:
                r = l

            profit = max(profit, prices[r] - prices[l])

        return profit
        
            