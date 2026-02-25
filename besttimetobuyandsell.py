class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
'''class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        seen=[]
        for i in range(len(prices)):
            for j in range(i,len(prices)-1):
                if prices[i] < prices[j+1]:
                    seen.append(prices[j+1]-prices[i])
        if seen:
           return max(seen)
        else:
            return 0

        
        
        
runn=Solution()
print(runn.maxProfit([7,2,4,6]))
print(runn.maxProfit([7,6,4,3,1]))
num=[2,3,4,5]
print(num[-1])'''