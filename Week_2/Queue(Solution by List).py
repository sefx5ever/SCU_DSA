#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue) == 0:
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

