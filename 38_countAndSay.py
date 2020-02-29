class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seg = "1"
        for i in range(n-1):
            seg = self.nextSeq(seg)
        return seg
    
    def nextSeq(self,seg):
        i, next_seg = 0, ""
        
        while i < len(seg):
            count = 1
            while i < len(seg)-1  and seg[i] == seg[i+1]:
                count += 1
                i += 1
            next_seg += str(count) + seg[i]
            i += 1
        return next_seg

test = Solution()
result = test.countAndSay(5)
print(result)

            