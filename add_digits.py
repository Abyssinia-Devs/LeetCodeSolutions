class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        j=0
        nums=[0,1,2,3,4,5,6,7,8,9]
        if num in nums:
            return num
        while num not in nums:
            seen=[]
            j=0
            while num>0:
                digit=num %10
                seen.append(digit)
                num=num//10
            for i in seen:
                    j+=i
            if j in nums:
                return j
            
            num=j
            
           
            

ruun=Solution()
print(ruun.addDigits(38))