#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
#    class Solution(object):
#        def permute(self, nums):
#            """
#            :type nums: List[int]
#            :rtype: List[List[int]]
#            """
#            from itertools import permutations
#            return list(permutations(nums))
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None or root==p or root==q:
            return root
        lt=self.lowestCommonAncestor(root.left, p, q)
        rt=self.lowestCommonAncestor(root.right, p, q)
        if lt!=None and rt!=None:
            return root
        elif lt==None:
            return rt
        else:
            return lt
if __name__ == '__main__':
    t=TreeNode()
    s=Solution()
    print s.lowestCommonAncestor(t)
    pass
