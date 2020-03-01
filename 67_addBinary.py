"""Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0."""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        result, carry, val = "", 0, 0  

        for i in range(max(len(a), len(b))):

            val = carry # collect carry from last loop

            if i < len(a):
                val += int(a[-(i+1)]) #start from the last digit
            if i < len(b):
                val +=  int(b[-(i+1)])
            
            carry, val = val // 2, val % 2
            result += str(val)
        if carry:
            result += str(1)
        return result[:: -1]  #return it reversely

test = Solution()
a = "1010"
b = "1010"
print(test.addBinary(a,b))



