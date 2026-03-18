nums = [2, 2, 3,3, 4, 3, 3, 2, 2, 3, 3]
counts={}
threshold=len(nums)//2
def get_majority(nums):
    for n in nums:
        counts[n]=counts.get(n,0) + 1
        if counts[n] > threshold:
            return n
        else:
           pass
print(f' the majority is {get_majority(nums)}')
nums = [2, 2, 3, 4, 3, 3, 2, 2, 3, 3]

