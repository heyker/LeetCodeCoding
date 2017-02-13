#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret=0
        k=x^y
        while k>0:
            ret+=(k&1)
            k>>=1
        return ret

if __name__ == '__main__':
    s=Solution()
    print s.hammingDistance(1,4)
    pass
