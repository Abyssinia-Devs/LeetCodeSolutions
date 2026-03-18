
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>=1:
            result=log(n,4)
            if result.is_integer():
                return True
            else:
                return False
        else:
            return False