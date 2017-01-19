#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def calcTwo(self,A,B):
        ret=dict()
        for i in A:
            for j in B:
                s=i+j
                if s not in ret:
                    ret[s]=0
                ret[s]+=1
        return ret
    
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        MAP_AB=self.calcTwo(A,B)
        MAP_CD=self.calcTwo(C,D)
        ret=0
        for i in MAP_AB:
            if -i in MAP_CD:
                ret+=(MAP_AB[i]*MAP_CD[-i])
        return ret
if __name__ == '__main__':
    s=Solution()
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    print s.fourSumCount(A,B,C,D)
    pass
