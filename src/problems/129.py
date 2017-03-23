#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allNum(self, root,p):
        ret=0
        curp=p*10+root.val
        if root.left!=None:
            #print '@',root.val,ret
            ret+=(self.allNum(root.left,curp))
        if root.right!=None:
            ret+=(self.allNum(root.right,curp))
            #print root.val,ret
        elif root.left==None and root.right==None:
            ret=curp
        return ret
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if None==root:
            return 0
        return self.allNum(root,0)
if __name__ == '__main__':
    s=Solution()
    root=TreeNode(4)
    t9=TreeNode(9)
    t0=TreeNode(0)
    t1=TreeNode(1)
    #root.left=t9
    #root.right=t0
    t9.right=t1
    print s.sumNumbers(root)
    pass