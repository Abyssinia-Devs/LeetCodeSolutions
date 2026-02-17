class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]== target:
                return i
            elif nums[i] !=target:
                if nums [i]> target:
                    return i
                    
                elif nums[len(nums)-1]< target:
                    return len(nums)
                    
runn=Solution() 
print(runn.searchInsert([1,3,5,6],5))