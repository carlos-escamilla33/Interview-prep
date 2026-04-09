def getConcatenation(nums):
    ans = []
    i = 0

    while i < 2:
        for num in nums:
            ans.append(num)
        i += 1
    
    return ans