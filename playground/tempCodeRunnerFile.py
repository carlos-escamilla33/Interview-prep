
def removeDuplicates(nums):
    L = 0

    for R in range(L + 1, len(nums)):
        if nums[L] == nums[R]:
            L += 1
        nums[L] = nums[R]
    
    return L, nums[:L]

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))