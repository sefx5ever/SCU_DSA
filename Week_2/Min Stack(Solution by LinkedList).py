#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 建立空間節點
class Node:
    def __init__(self,x):
        self.x=x
        self.next=None
        
## MinStack 以 LIFO 原則       
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head=None
        self.tail=None
        self.min=None
        self.size=0

    ## 考慮因素：
    ## 1. 若空間節點不存在，則新建節點
    ## 2. 在新增同時，進行大小判斷
    def push(self, x: int) -> None:
        new=Node(x)   
        if self.size==0:
            self.head=new
            self.tail=self.head
            self.min=new.x
        else:
            self.head.next=new
            self.head=new
            if x < self.min:
                self.min=x
        self.size+=1
        return
    
    ## 考慮因素
    ## 1. 若空間節點不存在，則return -1
    ## 2. 若節點長度為1，代表刪除後將歸None
    ## 3. 若正常情況下，也將進行大小判斷
    def pop(self) -> None:
        if(self.size<=0):
            return -1
        elif(self.size==1):
            self.tail=None
            self.head=None
            self.min =None
            self.size=0
            return
        else:
            current=self.tail
            for num in range(self.size-1):
                prev=current
                current=current.next
                if(num==self.size-2):
                    if(num==0):
                        if(prev.x>current.x):
                            self.min=prev.x
                        self.head=prev
                    prev.next=None
                    current=None
                    self.head=prev
                    self.size-=1
                    return
                if(num==0):
                    if(prev.x<current.x):
                        self.min=prev.x
                    else:
                        self.min=current.x
                else:
                    if(self.min>current.x):
                        self.min=current.x

                   
    def top(self) -> int:
        return self.head.x

    def getMin(self) -> int:
        return self.min


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

