#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def __init__(self):
        self.kbs=[]
        self.kbs.append(set('qwertyuiop'))
        self.kbs.append(set('asdfghjkl'))
        self.kbs.append(set('zxcvbnm'))
        #print self.kbs[2]
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret=[]
        for i in words:
            kb=set(i.lower())
            for j in self.kbs:
                if kb.issubset(j):
                    ret.append(i)
                    break
        return ret
if __name__ == '__main__':
    s=Solution()
    wd=["Hello", "Alaska", "Dad", "Peace"]
    print s.findWords(wd)
    pass
