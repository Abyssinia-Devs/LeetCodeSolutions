class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = format(n, '032b')
        
        binaryrevrse=binary[::-1]
        return int(binaryrevrse,2)
runn=Solution()
print(runn.reverseBits(43261596))

