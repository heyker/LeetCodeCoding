#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getTreeSize(self,root):
        if root==None:
            return 0
        return 1+self.getTreeSize(root.left)+self.getTreeSize(root.right)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root==None:
            return 0
        lcnt=self.getTreeSize(root.left)
        if lcnt+1==k:
            return root.val
        if lcnt>=k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-lcnt-1)
if __name__ == '__main__':
    s=Solution()
    print s.combinationSum3(3,15)
    pass

