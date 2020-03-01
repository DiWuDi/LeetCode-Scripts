

#Runtime: 1116 ms, faster than 23.61% of Python3 online submissions for Two Sum.
#Memory Usage: 13.7 MB, less than 88.37% of Python3 online submissions for Two Sum.
  
 
class Solution:
    def twoSum(self, nums, target):
    
        # :type:nums: List[int], 
        #:type:target: int
        # :rtype:List[int]
        
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return ([dic[target - nums[i]],i])
        
            
    
s = Solution()
a = s.twoSum([3,2,3],6)
print(a)




"""
# The following is wrong, giving the wrong answer. cannot handle a list with 2 the smae 
#items. Reason: need to delet one if picked up

def twoSum(nums, target):
    for i in nums:
            next_index = nums.index(i)+1
            l = len(nums)
            j = nums[next_index]
            for next_index in range(next_index,l):
                if (i+j ) == target:
                    return([nums.index(i), next_index])
                next_index += 1
                
nums = [2, 7, 11, 15]
target = 9          
a = twoSum(nums,target)
print(a)

"""
