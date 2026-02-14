class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            elif nums[i] in seen:
                nums.remove(nums[i])
        k=len(nums)
       
        return k


runn=Solution()
#print(runn.removeDuplicates([1,2,1]))

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
        k=len(seen)
        return k
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

run=Solution()
print(run.removeDuplicates([1,1,1,1,1,2]))

