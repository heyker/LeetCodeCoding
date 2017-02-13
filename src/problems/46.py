#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self,nums):
        strnum=[]
        for i in nums:
            strnum.append(str(i))
        strnum.sort(lambda x,y:cmp(int(y+x), int(x+y)))
        ret=''.join(strnum).lstrip('0')
        if ret=='':
            ret='0'
        return ret
if __name__ == '__main__':
    s=Solution()
    nums=[3, 30, 34, 5, 9]
    print s.largestNumber(nums)
    pass
