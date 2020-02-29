"""Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = max(nums)
        if len(nums) >1:
            for i in range(len(nums) ):
                for j in range(i+1, len(nums)+1):
                    if sum(nums[i:j]) > max_ :
                        max_ = sum(nums[i:j])
        return max_

result = Solution()
test = [-2,1,-3,4,-1,2,1,-5,4]
#test1= [-1]
#test2=[2,1]
#number, number1, number2 = result.maxSubArray(test), result.maxSubArray(test1),result.maxSubArray(test2)

#print (number, number1, number2)

