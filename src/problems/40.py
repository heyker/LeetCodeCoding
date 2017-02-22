#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def DFS(self,start,arr,target,cur,res):
        #print start,len(arr),target,cur
        if target==0:
            res.append(cur[:])
            return
        if target<0 or start>=len(arr):
            return
        for i in range(start,len(arr)):
            if i>start and arr[i]==arr[i-1]:
                continue
            cur.append(arr[i])
            self.DFS(i+1,arr,target-arr[i],cur,res)
            cur.pop()
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        cur=[]
        if candidates==None or len(candidates)==0:
            return []
        candidates.sort()
        self.DFS(0,candidates,target,cur,res)
        return res
if __name__ == '__main__':
    s=Solution()
    c=[1,2,3,4,5,6,7,8,9]
    t=15
    print s.combinationSum2(c,t)
    pass

