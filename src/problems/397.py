#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        newn=long(n)
        cnt=0
        while newn>1:
            cnt+=1
            if newn&1:
                if newn&2 and newn!=3:
                    newn+=1
                else:
                    newn-=1
            else:
                newn>>=1
        return cnt
if __name__ == '__main__':
    s=Solution()
    n=15
    print s.integerReplacement(n)
    pass
