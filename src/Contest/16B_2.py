#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def __init__(self):
        self.a=None
        self.s=[[-1]*22]*22
    def prints(self):
        for i in self.s[0:4]:
            print i[0:4]
        print '###############'
    def DFS(self,l,r,who):
        print '#1---',l,r,who,self.s[0][1]
        if self.s[l][r] >=0:
            return self.s[l][r]
        if l==r and not who:
            self.s[l][r]=self.a[l]
            return self.a[l]
        if l==r and who:
            self.s[l][r]=0
            return 0
        if who==False:
            print l,r,self.s[0][1],who,'#1'
            self.s[l][r]=max(self.DFS(l+1,r,True)+self.a[l], self.DFS(l,r-1,True)+self.a[r])
            print l,r,self.s[0][1],who,'#2'
            return self.s[l][r]
        else:
            print l,r,self.s[0][1],who,'#3'
            self.s[l][r]=min(self.DFS(l+1,r,False),self.DFS(l,r-1,False))
            print l,r,self.s[0][1],who,'#4'
            return self.s[l][r]
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.a=nums
        all=0
        for i in nums:
            all+=i
        sum=self.DFS(0,len(nums)-1,False)
        print sum,all-sum
        if sum+sum >= all:
            return True
        return False
        
if __name__ == '__main__':
    s=Solution()
    arr=[1, 5, 2]
    print s.PredictTheWinner(arr)
    s.prints()
    pass
