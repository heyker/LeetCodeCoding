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
    def __init__(self):
        self.sum=dict()
    def visit(self,root):
        if root==None:
            return 0
        lv=self.visit(root.left)
        rv=self.visit(root.right)
        ret=root.val+lv+rv
        if ret not in self.sum:
            self.sum[ret]=0
        self.sum[ret]+=1
        return ret
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.visit(root)
        maxt=-2
        ret=[]
        for i in self.sum:
            if maxt < self.sum[i]:
                maxt=self.sum[i]
        for i in self.sum:
            if maxt==self.sum[i]:
                ret.append(i)
        return ret
if __name__ == '__main__':
    s=Solution()
    root = TreeNode()
    print s.findFrequentTreeSum(root)
    pass
