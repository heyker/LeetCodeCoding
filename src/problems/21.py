#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        ret=None
        if l1.val<l2.val:
            ret=l1
            ret.next=self.mergeTwoLists(l1.next, l2)
        else:
            ret=l2
            ret.next=self.mergeTwoLists(l1, l2.next)
        return ret
if __name__ == '__main__':
    s=Solution()
    citations=[3, 0, 6, 1, 5]
    print s.hIndex(citations)
    pass

