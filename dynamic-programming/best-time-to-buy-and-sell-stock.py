class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0  

        lowest_price = float('inf') 
        highest_profit = 0  
        for i in range(len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            elif prices[i] - lowest_price > highest_profit:
                highest_profit = prices[i] - lowest_price  

        return highest_profit