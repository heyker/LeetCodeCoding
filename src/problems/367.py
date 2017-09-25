#encoding=utf-8
'''
Created on 2017年09月25日

@author: heyker
'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x=num
        while x*x>num:
            x=(x+num/x)/2
        return x*x==num
if __name__ == '__main__':
    s=Solution()
    print s.isPerfectSquare(16)
    pass
