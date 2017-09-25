/*************************************************************************
	> File Name: 232.cpp
	> Author: heyker
	> Mail: heyker.he@gmail.com 
	> Created Time: 2017年09月25日 星期一 15时42分12秒
 ************************************************************************/

#include<iostream>
#include<stack>
using namespace std;
class MyQueue 
{
private:
    stack<int> _old,_new;
    void shift()
    {
        if (this->_old.empty())
        {
            while(!this->_new.empty())
            {
                this->_old.push(_new.top());
                _new.pop();
            }
        }
    }
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        this->_new.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int ret=0;
        this->shift();
        if(!this->_old.empty())
        {
            ret=this->_old.top();
            this->_old.pop();
        }
        return ret;
    }
    
    /** Get the front element. */
    int peek() {
        int ret=0;
        this->shift();
        if(!this->_old.empty())
        {
            ret=this->_old.top();
        }
        return ret;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return this->_old.empty() && this->_new.empty();
    }
};


//Your MyQueue object will be instantiated and called as such:
int main()
{
    MyQueue obj = new MyQueue();
    obj.push(1);
    obj.push(2);
    int param_2 = obj.pop();
    int param_3 = obj.peek();
    bool param_4 = obj.empty();
}



