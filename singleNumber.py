class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=[]
        for i in (nums):
            if nums.count(i)== 1:#if nums.count(i)-1==0:
               return i
runn=Solution()
print(runn.singleNumber([1,2,2,2,4,3,3,4,5,5]))