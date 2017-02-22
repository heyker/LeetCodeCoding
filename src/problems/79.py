#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def DFS(self, board, word,i,j,s,v,d):
        #print i,j,s,v

        if i<0 or i>=len(board):
            return False
        if j<0 or j>=len(board[i]):
            return False
        if board[i][j] != word[s]:
            return False
        if s==len(word)-1:
            return True
        for jp in d:
            ni=i+jp[0]
            nj=j+jp[1]
            md=ni+nj*len(board)
            if md in v:
                continue
            v.add(md)
            if self.DFS(board, word, ni, nj, s+1, v, d):
                return True
            v.remove(md)
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        v=set()
        s=0
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        ret=False
        if word==None or board==None:
            return ret
        if len(word)<1 or len(board)<0:
            return ret
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j]==word[0]:
                    v.clear()
                    v.add(i+j*len(board))
                    ret=self.DFS(board, word, i, j, s, v,d)
                    if ret==True:
                        return ret
        return False
if __name__ == '__main__':
    s=Solution()
    board=[
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    board=['aa']
    print s.exist(board, "aaa")
    pass

