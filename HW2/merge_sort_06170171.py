#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    # 該區將list切成用list組成的一個number後，執行merge function
    def mergeSort(self,list_):
        len_ = len(list_)  # 取出某情況時，list之總長度
        if (len_ < 2): # 設定條件機制，當達到一個list中只有一個number時，
            return     # 跳出該遞迴
        splitpoint = len_ // 2 # 用公式取出中心點，用以分割左右list
        left = list_[:splitpoint]   # list【左】
        right = list_[splitpoint:]  # list【右】
        self.mergeSort(left)        # 用以分割list中左半部
        self.mergeSort(right)       # 用以分割list中右半部
        self.merge(list_,left,right)# 當最終遞迴結束後，開始往回執行merge function
     
    # 該區將list用一對一比較形式，完成該遞迴之合併
    def merge(self,list_,left,right):
        countL,countR,send = 0,0,0 # 每次進入此function時，重計步數
        
        # 在進入loop前，確認目前負責count L和 R的數不超過 left/right List之長度
        while (countL < len(left) and countR < len(right)):
            if (left[countL] <= right[countR]): # 兩個list間之比較（包括兩數相同）
                list_[send] = left[countL] 
                countL+=1
                send+=1
            else:                               # 不符合上述條件時執行
                list_[send] = right[countR]
                countR+=1
                send+=1
                
        while (countL < len(left)): # 當left之長度大於right時執行
            list_[send] = left[countL]
            countL+=1
            send+=1
            
        while (countR < len(right)): # 當right之長度大於left時執行
            list_[send] = right[countR]
            countR+=1
            send+=1
  
# Reference: 
# https://www.youtube.com/watch?v=6pV2IF0fgKY&t=141s
# https://www.youtube.com/watch?v=mB5HXBb_HY8&t=444s
# https://www.youtube.com/watch?v=ak-pz7tS5DE&t=26s
