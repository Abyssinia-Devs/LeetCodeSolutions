
class Solution(object):
    def climbStairs(self, n):
        if n==1 or n==2:
            return 1
        first=1
        second=2
        for i in range(3, n+1):
            first,second=second,first +second
        return second
runn=Solution()
print(runn.climbStairs(4))
"""def fibonanci(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return(fibonanci(n-1)+fibonanci (n-2))
print(fibonanci(4))"""