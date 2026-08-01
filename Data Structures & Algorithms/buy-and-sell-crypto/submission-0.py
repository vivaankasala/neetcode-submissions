class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        diff=0


        min_price=prices[0]
        for price in prices:
            min_price=min(min_price,price)
            diff=max(diff,price-min_price)
        return diff
        