#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret=[]
        n1=sorted(nums1)
        n2=sorted(nums2)
        i1=0;i2=0;
        while i1<len(n1) and i2<len(n2):
            if n1[i1]==n2[i2]:
                ret.append(n1[i1])
                i1+=1
                i2+=1
            elif n1[i1]>n2[i2]:
                i2+=1
            elif n1[i1]<n2[i2]:
                i1+=1
        return ret
if __name__ == '__main__':
    s=Solution()
    nums1 = [1, 2, 2, 1]; nums2 = [2, 2]
    #nums1 = [1, 2, 2, 1]; nums2 = []
    print s.intersect(nums1,nums2)
    pass

