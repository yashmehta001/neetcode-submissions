class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        while i<len(prices):
            j = i
            buying_price = prices[i]
            while j<len(prices):
                selling_price = prices[j]
                j+=1
                if buying_price > selling_price:
                    continue
                profit = selling_price - buying_price
                max_profit = max(profit , max_profit)
                
            i +=1
        

        return max_profit
        