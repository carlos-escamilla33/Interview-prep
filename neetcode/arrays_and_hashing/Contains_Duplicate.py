# Space Complexity - O(N), because we are appending n nums into the set
# Time Complexity - O(N), because we may have to go through the entire array for us to be able to find a duplicate, 
#                       or we can go through the entire array without finding a duplicate

def hasDuplicate(nums):
    nums_set = set()

    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)
    
    return False
