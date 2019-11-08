#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):     
    def heapSort(self,list_):
        self.list_ = list_
        self.maxHeap()
        
    # 使用 Max Heap方式，每次list中0位置必須在heapify後為list中最大之數
    def maxHeap(self):
        len_ = len(self.list_)  # list 總長度
        parent = (len_-1)//2    # 找出父節點之公式
        
        # 在loop過程中，主要功能是形成小三角（堆），並在其中進行父子節點之大小判斷
        for index in range((parent-1),-1,-1):
            self.heapify(index,len_)
        
        # 在上述loop結束後，即完成一次整理堆的工作，
        # 所以需要把 0位置之值與目前最後位置進行互換，
        # 然後，將需要進行loop的長度-1
        for index in range((len_-1),-1,-1):
            self.list_[0],self.list_[index] = self.list_[index],self.list_[0]
            self.heapify(0,index)
    
    # 用heap形式進行maxHeap小到大排列
    def heapify(self,index,len_):
        if (index > len_):      # 堆積排列到底層時，不會再需要排列的必要，
            return              # 因此設定防止機制
        i = index               # 父節點
        left = 2*i + 1          # 子節點【左】
        right = 2*i + 2         # 子節點【右】
        
        # 之前碰過QuickSort迴圈機制設定，所以同樣道理，先進行前者條件再到後者，不可互換
        if (left < len_ and self.list_[left] > self.list_[i]):     
            i = left # 當左子節點小於總長度及左子節點大於父節點時，重新定義父節點位置
        
        # 之前碰過QuickSort迴圈機制設定，所以同樣道理，先進行前者條件再到後者，不可互換
        if (right < len_ and self.list_[right] > self.list_[i]):
            i = right # 當右子節點小於總長度及右子節點大於父節點時，重新定義父節點位置
        
        # 過程中，若執行過上述條件判斷時，意味著有子節點大於父節點的請款發生，故與初始父節點互換
        if (i != index):
            self.list_[i],self.list_[index] = self.list_[index],self.list_[i]
            self.heapify(i,len_) # 重新檢查機制，確保沒有子節點大於父節點情況

# Reference: https://www.youtube.com/watch?v=j-DqQcNPGbE
