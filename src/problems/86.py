#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def str(self):
        ret=str(self.val)
        cur=self.next
        while cur!=None:
            ret+=(' '+str(cur.val))
            cur=cur.next
        return ret
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less=None;curLess=None;
        large=None;curLarge=None;
        iterv=head
        while iterv !=None:
            if iterv.val<x:
                if curLess==None:
                    curLess=iterv
                    less=iterv
                else:
                    curLess.next=iterv
                    curLess=iterv
            else:
                if curLarge==None:
                    curLarge=iterv
                    large=iterv
                else:
                    curLarge.next=iterv
                    curLarge=iterv
            iterv=iterv.next
        if less==None:
            less=large
        else:
            curLess.next=large
        if curLarge!=None:
            curLarge.next=None
        return less
if __name__ == '__main__':
    so=Solution()
    ln=ListNode(2)
    ln.next=ListNode(1)
    #print ln.str()
    print '123',so.partition(ln,2).str()
    print 'over~'
