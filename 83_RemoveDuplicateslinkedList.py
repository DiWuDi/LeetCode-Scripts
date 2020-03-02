"""Given a sorted linked list, delete all duplicates such that each element appear only once.
Input: 1->1->2
Output: 1->2"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode):
        #rtype: V -> ListNode

        curr = head 
      
        while curr:
            runner = curr.next
            while runner and runner.val == curr.val:
                runner = runner.next
            curr.next = runner
            curr = runner

        return head

head_ = ListNode(1)
e1 = ListNode(1)
e2 = ListNode(2)
head_.next = e1
e1.next = e2
result = Solution()
v = result.deleteDuplicates(head_)
# print the returned list
while v:
    print(v.val)
    v = v.next
