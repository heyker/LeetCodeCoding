#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findFight(self,i,l,r):
        #print i,l,r
        if l>r:
            return -1
        if self.lt[l]>=i:
            return l
        if self.lt[r]<i or l==r:
            return -1
        mid = (l+r)/2
        cur=self.findFight(i, l, mid)
        if cur==-1:
            cur=self.findFight(i, mid+1, r)
        return cur
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        ret=[]
        if len(intervals)==0:
            return ret
        self.m=dict()
        rt=[]
        for i in range(len(intervals)):
            rt.append(intervals[i].end)
            self.m[intervals[i].start]=i
        self.lt=sorted(self.m.keys())
        for i in rt:
            k=self.findFight(i,0,len(self.lt)-1)
            if k==-1:
                ret.append(-1)
            else:
                ret.append(self.m[self.lt[k]])
                
        return ret
if __name__ == '__main__':
    s=Solution()
    c=[]
    c.append(Interval(3,4))
    c.append(Interval(2,3))
    c.append(Interval(1,2))
    print s.findRightInterval(c)
    pass

