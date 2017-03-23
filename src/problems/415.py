#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret=''
        add=0
        n1=len(num1)-1
        n2=len(num2)-1
        
        while n1>=0 or n2>=0:
            if n1>=0:
                add+=int(num1[n1])
            if n2>=0:
                add+=int(num2[n2])
            ret=str(add%10)+ret
            add/=10
            n1-=1
            n2-=1
        if add>0:
            ret=str(add)+ret
        return ret
if __name__ == '__main__':
    s=Solution()
    print s.addStrings('1','9')
    pass