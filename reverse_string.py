
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.s=[]
        j=0
        for i in s[::-1]:
          s[j]=i
          j+=1
        return s
            
        
soo=Solution()
stt=['h','l','k']
ll=soo.reverseString(stt)
print(ll)
