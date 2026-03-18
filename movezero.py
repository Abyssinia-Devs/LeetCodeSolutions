# This function moves all zeroes in the list to the end.
# The order of non-zero elements stays the same.
#
# How it works:
# 1. We keep a pointer called insert_pos to track where the next non-zero number should go.
# 2. We loop through the list:
#    - If the number is not zero, we place it at insert_pos and move insert_pos forward.
# 3. After placing all non-zero numbers, we fill the remaining positions with zeroes.
# 4. The list is modified in-place (no new list is created).

def moveZeroes(nums):
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


# Example
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
