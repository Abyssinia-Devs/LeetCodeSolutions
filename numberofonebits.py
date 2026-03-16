class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (bin(n)).count('1')
runn=Solution()
fjk=runn.hammingWeight(11)
print(fjk)