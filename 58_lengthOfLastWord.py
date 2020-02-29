"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only."""

class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
     
        count, local = 0, 0 

        for i in range(len(s)):
            if s[i] == " ":
                local = 0
            else:
                local += 1
                count = local # use count to store the local count till the end
                
      
        return count



rt = Solution()
ss = "a dog "
print(rt.lengthOfLastWord(ss))



