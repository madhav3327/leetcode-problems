#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [2,7,11,15]
target = 9
for n in range(len(nums)):
    for m in range(len(nums)):
        if(n!=m) and nums[n]+nums[m]==target:
            print( n,m)
    break