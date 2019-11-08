#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 創建獨立空間（空值）
class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
        
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.size=0
    
    ## 考慮因素
    ## 1. 變數index可能小於 0,無法獲取該位置之值
    ## 2. 變數index大於等於現有LinkedList長度,因此無法得到位置
    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0 or index>=self.size:
            return -1
        current=self.head
        while(index>0):
            current=current.next
            index-=1
        return current.val
    
    ## 考慮因素
    ## 1. self.head可能已經存在,故插入於現有self.head前
    ## 2. self.head可能為空值，因此建立節點空間作為LinkedList之第一位置（Head）
    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new=Node(val)
        new.next=self.head
        self.head=new
        self.size+=1
        return
    
    ## 考慮因素
    ## 1. self.size等於0,目前無任何節點空間存在,因此直接建立節點空間
    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        current=self.head
        if self.size is 0:
            current=Node(val)
            self.size=1
            return
        while(current.next!=None):
            current=current.next
        current.next=Node(val)
        self.size+=1
        return

    ## 考慮因素
    ## 1. 變數index可能小於等於0,此時皆為0,並當作加入第一位置執行
    ## 2. 變數index大於等於現有LinkedList長度,因此無法得到位置
    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index>self.size:
            return
        elif index<=0:
            new=Node(val)
            new.next=self.head
            self.head=new
            self.size+=1
        else:
            current=self.head
            while(index>0):
                prevNode=current
                current=current.next
                index-=1
            new=Node(val)
            prevNode.next=new
            new.next=current
            self.size+=1
            return
        
    ## 考慮因素
    ## 1. 可能要刪除之index小於0,因此不成立
    ## 2. 變數index大於等於現有LinkedList長度,因此無法得到位置
    ## 3. 現有self.size可能為0,故無節點空間存在,無法刪除
    ## 4. 變數index為0時,且self.size大於0時,self.head值可被刪除 
    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or index>=self.size or self.size==0:
            return
        elif index==0:
            self.head.val=None
            self.head=self.head.next
            self.size-=1
            return
        else:
            current=self.head
            self.size-=1
            while(index>0):
                prevNode=current
                current=current.next
                index-=1
            prevNode.next=current.next
            current=None
            return 


# In[2]:


MyLinkedList=MyLinkedList()
MyLinkedList.addAtHead(1)
MyLinkedList.addAtTail(3)
MyLinkedList.addAtIndex(1, 2) # linked list becomes 1->2->3


# In[3]:


MyLinkedList.get(1)        


# In[4]:


MyLinkedList.deleteAtIndex(1)  # now the linked list is 1->3


# In[5]:


MyLinkedList.get(1)

