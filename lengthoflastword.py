class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split()
        for i in range (len(s)):
            if s[i]==s[len(s)-1]:
                return len(s[i])
runn=Solution()
print(runn.lengthOfLastWord('Hello world'))
print(runn.lengthOfLastWord( "   fly me   to   the moon  "))
