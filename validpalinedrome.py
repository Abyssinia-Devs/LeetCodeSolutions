class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ''.join(c for c in s if c.isalnum()).lower()
        
        if clean== clean[::-1]:
            return True
        else:
            return False
