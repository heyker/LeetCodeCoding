#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ar=[0]*len(num1+num2)
        for i in range(len(num1)-1,-1,-1):
            k1=int(num1[i])
            idx1=len(num1)-1-i
            for j in range(len(num2)-1,-1,-1):
                k2=int(num2[j])
                idx2=len(num2)-1-j
                ar[idx1+idx2]+=(k1*k2)
                #print idx1,idx2,ar
        ret=''
        for i in range(0,len(ar)-1):
            ar[i+1]+=(ar[i]/10)
            ar[i]%=10
            #print ar
            ret=str(ar[i])+ret
        ret=str(ar[-1])+ret
        ret=ret.lstrip('0')
        if ret=='':
            ret='0'
        return ret
if __name__ == '__main__':
    s=Solution()
    print s.multiply("999",'999')
    pass