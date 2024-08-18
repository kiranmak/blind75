import sys
# approach:
# start with first index and add it all non-adj. start + start +2,...
# then do next
def non_adjacent_sum(nums):

    def dp(index):
        if index >= len(nums):
            return 0 # or 0
        if index + 2 >= len(nums):  # last non-adjascent
            return nums[index] 

        sum = 0
        for ii in range(index+2, len(nums)):
            res = dp(ii)
            res+= nums[index]
            sum = max(res, sum)
        return sum

    maxsum = -sys.maxsize
    for i in range(len(nums)):
        sum = dp(i)
        print(f"out: index={i}, sum={sum}")
        maxsum = max(maxsum, sum)
    return maxsum
            
nums = [2, 4, 5, 12, 7]
print(non_adjacent_sum(nums)) # -> 16

'''
[2,4,5,12,7]
2 + 5 + 7
2 + 12
  4 + 12
  4 + 7
    5 + 7
    

'''