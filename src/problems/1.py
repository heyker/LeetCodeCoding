#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return  [i,j]
        return [-1,-1]
if __name__ == '__main__':
    s=Solution()
    nums = [2, 7, 11, 15]
    target = 9          
    print s.twoSum(nums,target)
    pass
