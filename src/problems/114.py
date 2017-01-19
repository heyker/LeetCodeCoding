#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        if root.left!=None:
            self.flatten(root.left)
        if root.right!=None:
            self.flatten(root.right)
        if root.left==None:
            return
        lastRight=root.left
        while lastRight.right!=None:
            lastRight=lastRight.right
        lastRight.right=root.right
        root.right=root.left
        root.left=None

            
        

if __name__ == '__main__':
    test=[1,2,3,4,5,6,7,8,9]
    s=Solution(test)
    print s.shuffle()
    print s.reset()
    pass
