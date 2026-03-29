class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxprofit=0
        while r<len(prices):
            if prices[r]-prices[l]<0:
                l=r
                r=r+1
            else:
                maxprofit=max(maxprofit,prices[r]-prices[l])
                r=r+1
        return maxprofit







        