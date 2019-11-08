#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# In[2]:


MinStack=MinStack()
MinStack.push(-2)
MinStack.push(0)
MinStack.push(-3)


# In[3]:


MinStack.getMin()


# In[4]:


MinStack.pop()


# In[5]:


MinStack.top()


# In[6]:


MinStack.getMin()

