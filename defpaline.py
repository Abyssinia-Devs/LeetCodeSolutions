class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x=str(x)
        if (self.x[0:]) == (self.x[::-1]):
            return True
        else :
            return False
x_value=Solution()
x_value.isPalindrome(121)
x_value.isPalindrome(-121)
x_value.isPalindrome(10)
