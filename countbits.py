class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        index=[]

        for i in range(n+1):
            index.append(bin(i).count('1'))
        return (index)
        