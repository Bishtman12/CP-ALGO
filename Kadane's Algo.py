import sys
def solve(nums):
    cur_sum = 0
    max_sum = sys.maxsize*(-1)
    for i in range(len(nums)):
        if cur_sum + nums[i] >= cur_sum:
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)
        else:
            cur_sum = 0
    return max_sum

nums = [1]
print(solve(nums))
