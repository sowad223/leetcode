class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        m=prices.copy()
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    m[i]=prices[i]-prices[j]
                
                    break
        return m

        