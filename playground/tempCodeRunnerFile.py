import math

def containsDuplicate(nums):
    count = {}

    for n in nums:
        if n not in count:
            count[n] = 0
        count[n] += 1

        if count[n] == 2:
            return True
    
    return False
    

arr = [1,2,3,4]

print(containsDuplicate(arr))