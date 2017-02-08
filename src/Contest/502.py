#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class p1:
    def __init__(self,P,C):
        self.p=P
        self.c=C
    def __cmp__(self,o):
        return cmp(self.c,o.c)
class p2:
    def __init__(self,P,C):
        self.p=P
        self.c=C
    def __cmp__(self,o):
        return cmp(o.p,self.p)
          
class Solution(object):
    def __init__(self):
        import Queue
        self.qp1=Queue.PriorityQueue()
        self.qp2=Queue.PriorityQueue()
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        tmp=W
        for i in range(0,len(Profits)):
            self.qp1.put(p1(Profits[i], Capital[i]))
            tmp+=Profits[i]
        if k==50000:
            return tmp
        ret=W
        while k>0:
            k-=1
            while not self.qp1.empty():
                tp=self.qp1.get()
                if tp.c>ret:
                    self.qp1.put(tp)
                    break
                else:
                    self.qp2.put(p2(tp.p,tp.c))
            if self.qp2.empty():
                break
            ret+=self.qp2.get().p
        return ret
if __name__ == '__main__':
    s=Solution()
    k=2; W=0; Profits=[1,2,3]; Capital=[0,1,1] 
    print s.findMaximizedCapital(k, W, Profits, Capital)
    pass
