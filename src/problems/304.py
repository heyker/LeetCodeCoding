#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix)==0:
            self.sumMatix=None
            return
        lenc=len(matrix[0])
        lenr=len(matrix)
        self.sumMatix= matrix#[[0 for col in range(lenc)] for row in range(lenr)]
        for i in range(lenr):
            csum=0
            for j in range(lenc):
                csum+=matrix[i][j]
                self.sumMatix[i][j]=csum
                if i>0:
                    self.sumMatix[i][j]+=self.sumMatix[i-1][j]
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.sumMatix==None:
            return 0
        r1=self.sumMatix[row2][col2]
        if row1>0:
            r1-=self.sumMatix[row1-1][col2]
        if col1>0:
            r1-=self.sumMatix[row2][col1-1]
            if row1>0:
                r1+=self.sumMatix[row1-1][col1-1]
        return r1

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
if __name__ == '__main__':
    matrix=[
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]]
    s=NumMatrix(matrix)
    print s.sumRegion(1, 2, 2, 4)
    pass
