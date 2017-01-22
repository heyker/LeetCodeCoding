#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        neworder=''
        for i in preorder.split(','):
            if i=='#':
                neworder+='#'
            else:
                neworder+='@'
        while '@##' in neworder:
            neworder=neworder.replace('@##', '#')
        return neworder=='#'
if __name__ == '__main__':
    s=Solution()
    preorder='9,3,4,#,#,1,#,#,2,#,6,#,#'
    print s.isValidSerialization(preorder)
    pass