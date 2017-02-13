#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ret=[]
        for i in tokens:
            if i in ['+','-','*','/']:
                s1=ret.pop()
                s2=ret.pop()
                if i=='+':
                    ret.append(s2+s1)
                elif i=='-':
                    ret.append(s2-s1)
                elif i=='*':
                    ret.append(s2*s1)
                elif i=='/':
                    f=1
                    if s1<0:
                        s1*=-1
                        f*=-1
                    if s2<0:
                        s2*=-1
                        f*=-1
                    ret.append(s2/s1*f)
            else:
                ret.append(int(i))
        return ret[0]
if __name__ == '__main__':
    s=Solution()
    c=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print s.evalRPN(c)
    pass

