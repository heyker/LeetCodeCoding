#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m=len(dungeon)
        n=len(dungeon[0])
        curt=[10000000]*n
        curt[n-1]=1
        for i in range(m-1,-1,-1):
            l=dungeon[i]
            
            curt[n-1]-=l[n-1]
            if curt[n-1]<=0:
                curt[n-1]=1
            for i in range(n-2,-1,-1):
                curt[i]=min(curt[i+1],curt[i])-l[i]
                if curt[i]<=0:
                    curt[i]=1
            #print curt
        return curt[0]
    
if __name__ == '__main__':
    so=Solution()
    dungeon=[[0,-3]]
#        [[-2,-3,3],
#                 [-5,-10,1],
#                 [10,30,-5]]
    print so.calculateMinimumHP(dungeon)
