class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        resulta=0
        resultb=0
        a=a[::-1]
        b=b[::-1]
        for i ,value in enumerate(a):
            resulta+=((2**i)*(int(value)))
        for j , valueb in enumerate(b):
            resultb+=((2**j) *(int(valueb)) )
        print(resulta,resultb)
        sum=bin(resulta +resultb)
        return sum[2:]
runn=Solution()
print(runn.addBinary("1000","1011"))