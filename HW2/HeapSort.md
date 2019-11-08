
# Heap Sort

1. ### Array Representation of Binary Tree
![](https://i.imgur.com/PscG1Q4.jpg)
2. ### ChatFlow
![](https://i.imgur.com/VZMIBIf.png)

Link to code page: https://github.com/sefx5ever/SCU_DSA/blob/master/HW2/heap_sort_06170171.py

### Flow Desription:
ARRAY = [4,1,3,2,16,14,8]
Step 1: 3 is swapped with 14.
Step 2: 1 is swapped with 16.
Step 3: Max heap is created and 4 is swapped with 16.
Step 4: 16 is disconnected from heap.
Step 5: Repeat Step

### Difficulties:
1. After some trial and error, I realized that the concept and mindset to code heap sort was slightly different, so I was stuck on the order of list when it turn to a binary tree.
2. I was unfamiliar with OOP, so I made majority of mistake on it and the rest just fine.
3. One of the difficulty is the way to drop and exchange at the same time in a loop, so I try to do my own at first, but I gave up in time and search and refer to the answer.

### Test:
![](https://i.imgur.com/WeYkXlv.png)

### Extra Description：
* #### Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.

* #### Example ：
(1) Node is at index : i
(2) Left Child is at : 2 * i + 1
(3) Right Child is at: 2 * i + 2
(4) Parent is at     : | i/2 |
(5) Full Binary Tree : 2 ^ (h + 1) - 1 of Nodes

* #### Let's say i = 2(B), then left child is at 4(D)[ 2 * 2 ], right child is at 5(E)[ 2 * 2 + 1 ]. To prove that the D and E is the child of B, so LEFT[ 4 / 2 = 2 ] or RIGHT[ |5 / 2| = 2 ]. This is a max complete binary tree so it has 7[ 2 ^ (2 + 1) - 1 ] of Nodes.

* #### The Condition of Complete Binary Tree ：
    * The height of binary - 1 is full element.
    * Last element are filled from left to right.

* #### Complexity
| Data Structure | Time Complexity[Average] | Time Complexity[Worst] |
| ------------- | ------------- | ------------- |
| Heap Sort | O(n log(n)) |  O(n log(n)) |

### References:
* https://www.youtube.com/watch?v=MtQL_ll5KhQ
* https://www.youtube.com/watch?v=2DmK_H7IdTo
* https://www.youtube.com/watch?v=7h1s2SojIRw&t=4s
* https://www.youtube.com/watch?v=-qOVVRIZzao&t=1s
* https://www.youtube.com/watch?v=HqPJF2L5h9U&t=1969s
* https://www.youtube.com/watch?v=j-DqQcNPGbE&t=1161s
* https://www.youtube.com/watch?v=k72DtCnY4MU
* https://www.youtube.com/watch?v=t0Cq6tVNRBA&t=435s
* http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html
