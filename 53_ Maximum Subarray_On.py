"""Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        
        globle_max, local_max = 0, 0
        for num in nums:
            local_max = max(0, local_max+num)  # 0--start over, otherwise keep the old set
            globle_max = max(globle_max, local_max)

        
        return globle_max

result = Solution()
test = [-2,1,-3,4,-1,2,1,-5,4]
result.maxSubArray(test)
# test1= [-1]
# test2=[2,1]
# number, number1, number2 = result.maxSubArray(test), result.maxSubArray(test1),result.maxSubArray(test2)

# print (number, number1, number2)

