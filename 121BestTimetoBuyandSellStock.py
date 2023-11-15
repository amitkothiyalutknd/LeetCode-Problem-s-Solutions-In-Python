# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice, profit = min(prices[0:2]), 0
        day = prices.index(minPrice)
        prices.append(0)
        for index in range(day, len(prices) - 1):   
            if prices[index+1] > minPrice:
                if prices[index+1] - minPrice > profit:
                    profit = prices[index+1] - minPrice
            else:
                minPrice = prices[index+1]
        return profit
        
sol = Solution()
prices = list(map(int, input(f"Enter The Prices For Stocks. Seperate Each Input From Single Space: ").strip().split()))[:]
print(f"Maximum Profit In {prices} is:\t", sol.maxProfit(prices))