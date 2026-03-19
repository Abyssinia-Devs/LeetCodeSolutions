
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        nums=list(nums)
        if len(nums)<3:
            return max(nums)

        nums=sorted(nums,reverse=True)
        return nums[2]
run=Solution()
nu=run.thirdMax([5,2,4,1,3,6,0])
print(nu)





''' class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        nums=list(nums)
        if len(nums)<3:
            return max(nums)
        trial=2
        while trial:
            for i in nums:
                nums.remove(max(nums))
                trial-=1
        return max(nums)
run=Solution()
nu=run.thirdMax([5,2,4,1,3,6,0])
print(nu)'''