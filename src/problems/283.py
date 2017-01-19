#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        znum=0
        while 0 in nums:
            nums.remove(0)
            znum+=1
        nums+=([0]*znum)
               
if __name__ == '__main__':
    test=[1,0,3,0,5,6,7,8,9]
    s=Solution()
    s.moveZeroes(test)
    print test
    pass
