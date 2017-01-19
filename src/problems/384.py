#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data=nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.data

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        cdata=self.data[:]
        random.shuffle(cdata)
        return cdata
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
if __name__ == '__main__':
    test=[1,2,3,4,5,6,7,8,9]
    s=Solution(test)
    print s.shuffle()
    print s.reset()
    pass
