#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n=len(citations)
        cc=[0]*(n+1)
        for k in citations:
            if k >=n:
                k=n
            cc[k]+=1
        if cc[n]>=n:
            return n
        k=n-1
        while k>=0:
            cc[k]+=cc[k+1]
            if cc[k]>=k:
                return k
            k-=1
        return 0
if __name__ == '__main__':
    s=Solution()
    citations=[3, 0, 6, 1, 5]
    print s.hIndex(citations)
    pass

