# Definition for a binary tree node. Given two binary trees, write a function to check 
# if they are the same or not.
#Two binary trees are considered the same if they are structurally identical and the nodes
#  have the same value..

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p != None and q != None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False

p = TreeNode(1)
p1 = TreeNode(2)
p2 = TreeNode(1)
p.left = p1
p.right = p2

q = TreeNode(1)
q1 = TreeNode(2)
q2 = TreeNode(1)
q.left = q1
q.right = q2

test = Solution()
print(test.isSameTree(p,q))