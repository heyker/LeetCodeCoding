#encoding=utf-8
'''
Created on 2016年12月27日

@author: heyker
'''
class Solution(object):
    def __init__(self):
        self.ivd=set()
        self.vd=set()
    def checkVaild(self,s):
        if s in self.ivd:
            return False
        if s in self.vd:
            return True
        cnt=0
        for i in s:
            if i=="(":
                cnt+=1
            elif i==")":
                cnt-=1
                if cnt<0:
                    break
        if cnt==0:
            self.vd.add(s)
            return True
        self.ivd.add(s)
        return False
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret=set()
        cur=set()
        if self.checkVaild(s):
            ret.add(s)
        cur.add(s)
        while len(ret)==0:
            newstr=set()
            for o in cur:
                for i in range(0,len(o)):
                    if i>0 and o[i]==o[i-1]:
                        continue
                    elif o[i]=='(' or o[i]==')':
                        ns=o[:i]+o[i+1:]
                        if self.checkVaild(ns):
                            ret.add(ns)
                        else:
                            newstr.add(ns)
            cur=newstr 
        return list(ret)
if __name__ == '__main__':
    s=Solution()
    print s.removeInvalidParentheses('(a)())()')
    pass

