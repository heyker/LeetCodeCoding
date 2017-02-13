#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def cmp(self,a,b):
        ret=0
        for i in range(0,len(a)):
            if a[i]!=b[i]:
                ret+=1
                if ret>1:
                    break
        return ret==1
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        import Queue
        basket=Queue.Queue()
        basket.put((beginWord,0))
        store=set(wordList)
        if endWord not in store:
            return 0
        while not basket.empty():
            itm=basket.get()
            wd=itm[0]
            num=itm[1]
            if wd==endWord:
                return num+1
            for i in range(0,len(wd)):
                nd=list(wd)
                for j in [chr(c) for c in range(97,123)]:
                    if j==nd[i]:
                        continue
                    #print nd[i],j
                    nd[i]=j
                    k=''.join(nd)
                    if k in store:
                        basket.put((k,num+1))
                        store.remove(k)
        return 0
if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log" ,"cog"]
    s=Solution()
    print s.ladderLength(beginWord, endWord, wordList)
    pass
