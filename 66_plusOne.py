"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the
 array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself."""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:  #keep on checking if the current is 9
                digits[i] = 0
            else: 
                digits[i] += 1
                return digits  # return if not all 9
        digits[0] = 1
        digits.append(0)
        return digits



test = Solution()
str_ = [9,8,9]
print(test.plusOne(str_))