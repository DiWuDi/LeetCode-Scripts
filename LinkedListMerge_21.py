# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:59:02 2020

@author: DELL
"""
class ListNode:
     def __init__(self,x):
         self.val = x
         self.next = None
         
         
def mergeTwoLists(l1, l2):
    """
    

    Parameters
    ----------
    L1 : TYPE
        DESCRIPTION. ListNode
    L2 : TYPE
        DESCRIPTION.ListNode

    Returns Bool
    -------
    None.

    """
    
    curr = dummy = ListNode(0)
    
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        
    curr.next = l1 or l2
    
    return dummy.next

a = [1,2,3,4]
b = [1,3,5,6,7]
A = ListNode(a)
B = ListNode(b)
C = mergeTwoLists(A,B)
print(C.val)


            