class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
 
        s=list(s)
        t=list(t)
        seen=[]
        for i in t:
            if t.count(i) > s.count(i):
                return i
           


runn=Solution()
stri = "python"
t = "typhonq"
print(runn.findTheDifference(stri,t))

strr='abc'   
dd=list(stri)

#print(sorted(stri),sorted(t))

