#encoding=utf-8
'''
Created on 2016年12月22日
@author: heyker
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=set('aeiouAEIOU')
        head=0
        tail=len(s)-1
        nstr=list(s)
        while head<tail:
            swap=True
            if nstr[head] not in vowels:
                head+=1
                swap=False
            if nstr[tail] not in vowels:
                tail-=1
                swap=False
            
            if swap:
                nstr[head],nstr[tail]=nstr[tail],nstr[head]
                head+=1
                tail-=1
        return ''.join(nstr)
            
if __name__ == '__main__':
    s=Solution()
    tickets='leetcode'
    print s.reverseVowels(tickets)
    pass