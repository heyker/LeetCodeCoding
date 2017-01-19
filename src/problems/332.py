#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mp=dict()
        for ft in tickets:
            #ft[0],ft[1]
            if ft[0] not in mp:
                mp[ft[0]]=[]
            mp[ft[0]].append(ft[1])
        for i in mp:
            mp[i].sort()
        ret=[]
        num=len(tickets)+1;
        self.dfs('JFK', mp, ret,num)
        return ret
    def dfs(self,k,mp,ret,num):
        ret.append(k)
        #print ret
        if len(ret)==num:
            return True
        if k in mp:
            for i in range(0,len(mp[k])):
                nk=mp[k][i]
                if len(nk)==3:
                    mp[k][i]='####'
                    if self.dfs(nk,mp,ret,num):
                        return True
                    else:
                        mp[k][i]=nk
                        ret.pop()
        return False   
if __name__ == '__main__':
    s=Solution()
    tickets=[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print s.findItinerary(tickets)
    #a=['123','789','456']
    pass