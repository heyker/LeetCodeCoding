#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=dict()
        add=0
        ret=0
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            ret+=d[i]
            if d[i]%2!=0:
                add=1
                ret-=1
        return ret+add
                
if __name__ == '__main__':
    s=Solution()
    k='abccccdd'
    print s.longestPalindrome(k)
    pass