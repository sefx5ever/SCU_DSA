#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 建立一個空間節點
class Node:
    # 將初始化參數用self.（pointer）存取
    def __init__(self, data):
        self.data = data
        self.next = None # make None as the default value for next.
    # 計算目前節點數量
    def count_nodes(head):
        # assuming that head != None
        count = 1
        current = head
        while current.next is not None:
            current = current.next
            count += 1
        return count


# In[ ]:


# 建立每個節點
nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

# 針對每個節點從頭串起來
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print("This linked list's length is: (should print 5)")
print(count_nodes(nodeA))

