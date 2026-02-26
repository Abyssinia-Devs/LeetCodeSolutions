#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        return nums[len(nums)//2]


'''class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major=0
        for i in nums:
            if nums.count(i)>major:
                major=nums.count(i) 
        for i in nums:
            if nums.count(i)==major:
                return i
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major=nums.count(nums[0])
        maa=nums[0]
        for i in (nums):
            if nums.count(i)>major:
                major=nums.count(i)
                maa=i 
        return maa
    '''
