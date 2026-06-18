class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        buy_date = 0
        high = prices[0]
        profit = 0
        sell_date = 0
        for i in range(len(prices)):
            # if index's price is higher than high
            if low > prices[i]:
                low = prices[i]
                high = prices[i]
            if high < prices[i]:
                # we set high to the high
                high = prices[i]
            if high - low > profit:
                profit = high - low
        return profit
            

        