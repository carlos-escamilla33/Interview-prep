def twoSum(nums, target):
    ht = {}

    for i in range(len(nums)):
        x = target - nums[i]

        if x in ht:
            return [min(ht[x], i), max(ht[x], i)]
        else:
            ht[nums[i]] = i

# Time Complexity O(N), because we traverse the array only once
# Space Complexity O(N), because we populate the hashtable with N nums with their index as a value