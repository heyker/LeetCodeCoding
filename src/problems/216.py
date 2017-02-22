#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def DFS(self,start,arr,target,cur,res,k):
        #print start,len(arr),target,cur
        if target==0 and k==len(cur):
            res.append(cur[:])
            return
        if target<0 or start>=len(arr) or len(cur)>k:
            return
        for i in range(start,len(arr)):
            if i>start and arr[i]==arr[i-1]:
                continue
            cur.append(arr[i])
            self.DFS(i+1,arr,target-arr[i],cur,res,k)
            cur.pop()
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        cur=[]
        arr=[]
        if n<k or n>k*9:
            return []
        for i in range(1,10):
            #max_num=min(k,n/i)
            arr+=[i]
        #print arr
        self.DFS(0,arr,n,cur,res,k)
        return res
if __name__ == '__main__':
    s=Solution()
    print s.combinationSum3(3,15)
    pass

