def longestBalanced(nums):
    max_length = 0

    for i in range(len(nums)):
        evens_set = set()
        odds_set = set()

        for j in range(i, len(nums)):
            if nums[j] % 2 == 0:
                evens_set.add(nums[j])
            else:
                odds_set.add(nums[j])
            if len(evens_set) == len(odds_set):
                max_length = max(max_length, (j - i) + 1)
    
    return max_length

    

nums = [1,2,3,2]

print(longestBalanced(nums))