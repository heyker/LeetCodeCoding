#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area<=0:
            return [0,0]
        import math
        inter=int(math.sqrt(area))
        for i in range(inter,1,-1):
            if area%i==0:
                return [area/i,i]
        return [area,1]
if __name__ == '__main__':
    s=Solution()
    print s.constructRectangle(1)
    pass
