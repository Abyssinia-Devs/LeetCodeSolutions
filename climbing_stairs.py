class Solution(object):
    def climbStairs(self, n):
        """
        Returns the number of ways to climb n stairs.
        You can take 1 or 2 steps at a time.
        Uses an iterative Fibonacci approach.
        Time: O(n) | Space: O(1)
        """
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        first = 1
        second = 2

        for i in range(3, n + 1):
            first, second = second, first + second

        return second

"""def fibonanci(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return(fibonanci(n-1)+fibonanci (n-2))
print(fibonanci(4))"""