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
        #return ret
        return self.getInterval(ret)
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        return self.merge(intervals)
if __name__ == '__main__':
    s=Solution()
    t=[]
    t.append(Interval(1,2))
    t.append(Interval(3,5))
    t.append(Interval(6,7))
    t.append(Interval(8,10))
    t.append(Interval(12,16))
    for i in s.insert(t,Interval(4,9)):
        print i,
    pass

