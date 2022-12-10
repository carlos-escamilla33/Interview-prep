# hashmap leetcode problems

# 219 Contains Duplicate II 

def containsNearbyDuplicates(nums, k):
    numsDict = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in numsDict:
            j = numsDict[num]
            if abs(i - j) <= k:
                return True
        
        numsDict[num] = i
        
    return False