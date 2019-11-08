#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 建立空間節點
class Node:
    def __init__(self,x):
        self.x=x
        self.next=None
        
## Queue以FIFO為原則        
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.tail=None
    
    ## 考慮因素：
    ## 1. 若head不存在，代表需要建立第一項
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        new=Node(x)
        if(self.head==None):
            self.head=new
            self.tail=new
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=Node(x)
            self.tail=current.next
    
    ## 考慮因素：
    ## 1. 
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if(self.head==None):
            return -1
        else:
            current=self.head
            to_return=self.head.x
            if(current==self.tail):
                self.head=None
                self.tail=None
            else:
                self.head=current.next
                current=None
            return to_return

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.head.x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(self.head==None):
            return True
        else:
            return False


# In[2]:


MyQueue=MyQueue()
MyQueue.push(1)
MyQueue.push(2)


# In[3]:


MyQueue.peek()


# In[4]:


MyQueue.pop()


# In[5]:


MyQueue.empty()

