#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ng=[]
        m=len(grid[0])+2
        n=len(grid)+2
        ng.append([0]*m)
        for i in grid:
            ng.append([0]+i+[0])
        ng.append([0]*m)
        ret=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                if ng[i][j]==0:
                    continue
                ret+=(4-ng[i-1][j]-ng[i+1][j]-ng[i][j-1]-ng[i][j+1])
        return ret        
        
if __name__ == '__main__':
    grid=[[0,1,0,0],
          [1,1,1,0],
          [0,1,0,0],
          [1,1,0,0]]
    grid=[[1,0,0]]
    s=Solution()
    print s.islandPerimeter(grid)
    pass
