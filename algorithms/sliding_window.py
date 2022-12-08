# Sliding window leetcode problems

# 219 Contains Duplicate II 

def containsNearbyDuplicates(nums, k):
    L = k
    R = len(nums) - 1

    while L < R:
        absValue = abs(L - R)
        if nums[L] == nums[R] and absValue <= k:
            return True
        L+=1
        

    return False


nums = [1,2,3,1]

print(containsNearbyDuplicates(nums, 3))