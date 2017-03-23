#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        s=0
        e=len(nums)-1
        while s<=e:
            m=(s+e)/2
            #print s,m,e,nums[m]
            if nums[s]==target or nums[e]==target or nums[m]==target:
                return True
            if nums[s]<nums[m]:
                if target>nums[s] and target<nums[m]:
                    s=s+1
                    e=m-1
                else:
                    s=m+1
                    e=e-1
            elif nums[m]<nums[e]:
                if target<nums[e] and target>nums[m]:
                    s=m+1
                    e=e-1
                else:
                    s=s+1
                    e=m-1
            elif nums[e]==nums[m] or nums[s]==nums[m]:
                s=s+1
                e=e-1
            print s,e
        return False
if __name__ == '__main__':
    s=Solution()
    nums=[4,5,6,7,0,1,2]
    nums=[1,1,1,1,1,1,1,1,1,1,1]
    nums=[1,1,3,1]
    nums=[0,0,1,1,2,0]
    t=2
    print s.search(nums, t)
    pass
