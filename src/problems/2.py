#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        ret=str(self.val)
        nt=self.next
        while nt!=None:
            ret+=('->'+str(nt.val))
            nt=nt.next
        return ret
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curNode=None
        ret=None
        add=0
        c1=l1
        c2=l2
        while c1!=None or c2!=None:
            if c1!=None:
                add+=c1.val
                c1=c1.next
            if c2!=None:
                add+=c2.val
                c2=c2.next
            newnode=ListNode(add%10)
            if curNode==None:
                curNode=newnode
                ret=curNode
            else:
                curNode.next=newnode
                curNode=newnode
            add/=10
        if add>0:
            curNode.next=ListNode(add)
        return ret
if __name__ == '__main__':
    s=Solution()
    L10=ListNode(2)
    L11=ListNode(4)
    L12=ListNode(3)
    L10.next=L11
    L11.next=L12
    L20=ListNode(5)
    L21=ListNode(6)
    L22=ListNode(4)
    L20.next=L21
    L21.next=L22
    print s.addTwoNumbers(L10,L20)
    pass