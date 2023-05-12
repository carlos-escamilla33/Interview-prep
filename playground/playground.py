
def shuffle(nums, n):
    for i in range(n):
        nums[i]= nums[i] << 10
        nums[i] = nums[i] | nums[i+n] # this will store the x, y vals together in binary


    return