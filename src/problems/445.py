#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next=None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1=[]
        L2=[]
        L=[]
        cl1=l1
        cl2=l2
        while cl1!=None:
            L1.append(cl1.val)
            cl1=cl1.next
        while cl2!=None:
            L2.append(cl2.val)
            cl2=cl2.next
        ins=0
        while True :
            len1=len(L1)
            len2=len(L2)
            if len1+len2==0:
                break
            p1=0
            p2=0
            if len1>0:
                p1=L1.pop()
            if len2>0:
                p2=L2.pop()
            res=p1+p2+ins
            ins=res/10
            L.append(res%10)
        if ins>0:
            L.append(ins)
        ret=None
        for i in L:
            tmpNode=ListNode(i)
            tmpNode.next=ret
            ret=tmpNode
        return ret     
            
        
if __name__ == '__main__':
    a=[1,2]
    print a.pop()
    print a.pop()
    print a.pop()
    pass
