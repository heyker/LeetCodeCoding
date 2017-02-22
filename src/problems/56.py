#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Inter(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "["+str(self.start)+","+str(self.end)+"]"
    def __cmp__(self,t):
        return cmp(self.start,t.start)
    def merge(self,t):
        if self.end>=t.start:
            self.end=max(self.end,t.end)
            return True
        return False
class Solution(object):
    def getInter(self,intervals):
        ret=[]
        for i in intervals:
            ret.append(Inter(i.start,i.end))
        return ret
    def getInterval(self,inter):
        ret=[]
        for i in inter:
            ret.append(Interval(i.start,i.end))
        return ret
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret=self.getInter(intervals)
        ret.sort()
        flag=True
        while flag:
            flag=False
            i=0
            k=len(ret)
            while i<k-1:
                if ret[i].merge(ret[i+1]):
                    del ret[i+1]
                    k-=1
                    flag=True
                else:
                    i+=1
        return self.getInterval(ret)
if __name__ == '__main__':
    s=Solution()
    t=[]
    t.append(Interval(1,3))
    t.append(Interval(8,10))
    t.append(Interval(15,18))
    t.append(Interval(2,6))
    for i in s.merge(t):
        print i,
    pass

