import math

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        root=int(math.sqrt(num))
        if root * root==num:
            return True

        else:
            return False
        
        
        
        
        
ruu=Solution()
dd=ruu.isPerfectSquare(16) 
print(dd) 
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num=float(num ** (1/2))
        if num.is_integer():
            return True

        else:
            return False
        
        
ruu=Solution()
dd=ruu.isPerfectSquare(14) 
print(dd)    '''