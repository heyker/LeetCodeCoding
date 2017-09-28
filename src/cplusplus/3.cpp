/*************************************************************************
	> File Name: 232.cpp
	> Author: heyker
	> Mail: heyker.he@gmail.com 
	> Created Time: 2017年09月25日 星期一 15时42分12秒
 ************************************************************************/

#include<iostream>
using namespace std;
class Solution 
{
public:
    int lengthOfLongestSubstring(string s) 
    {
     int m[256]={0},ret=0,left=0;
     for(int i=0;i<s.size();++i)
     {
         if (m[s[i]]==0 || m[s[i]]<left)
         {
             ret=max(ret,i-left+1);
         }
         else
         {
             left=m[s[i]];
         }
         m[s[i]]=i+1;
     }
     return ret;   
    }
};

//Your MyQueue object will be instantiated and called as such:
int main()
{
    Solution obj =  Solution();
    cout<<obj.lengthOfLongestSubstring("1234");
}



