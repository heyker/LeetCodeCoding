#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        for i in s:
            i=i.upper()
            ret=(ret*26+ord(i)-ord('A')+1)
        return ret
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret=""
        while n>0:
            k=n%26
            if k==0:
                k=26
                n-=26
            ret=(chr(ord('A')+k-1))+ret
            n/=26
        return ret
if __name__ == '__main__':
    s=Solution()
    print s.titleToNumber('A')
    print s.convertToTitle(52)
    pass

