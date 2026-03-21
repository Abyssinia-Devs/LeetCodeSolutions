class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        indeces=[]
        for i in range(0,len(nums)) :
            n=bin(i)
            if n.count("1")==k:
                indeces.append(i)
        
        sum=0
        for i in (indeces):
            sum +=nums[i]
        return (sum)
runn=Solution()
runn.sumIndicesWithKSetBits([2,2],1)