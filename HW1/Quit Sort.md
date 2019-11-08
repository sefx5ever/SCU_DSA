# Quick Sort
![](https://i.imgur.com/xFhSDgb.jpg)

Link to code page ：https://nbviewer.jupyter.org/github/sefx5ever/SCU_DSA/blob/master/Week_3/Quick%20Sort.ipynb
### Flow Description：
1. Find a “pivot” item in the array. This item is the basis for comparison for a single round.
2. Start a pointer (the left pointer) at the first item in the array.
3. Start a pointer (the right pointer) at the last item in the array.
4. While the value at the left pointer in the array is less than the pivot value, move the left pointer to the right (add 1). Continue until the value at the left pointer is greater than or equal to the pivot value.
5. While the value at the right pointer in the array is greater than the pivot value, move the right pointer to the left (subtract 1). Continue until the value at the right pointer is less than or equal to the pivot value.
6. If the left pointer is less than or equal to the right pointer, then swap the values at these locations in the array.
7. Move the left pointer to the right by one and the right pointer to the left by one.
8. If the left pointer and right pointer don’t meet, go to step 1.

### Test：
![](https://i.imgur.com/pm54Lps.png)

### Extra Description：
* #### Complexity
| Data Structure | Time Complexity[Average] | Time Complexity[Worst] |
| ------------- | ------------- | ------------- |
| Quick Sort | O(n^2) |  O(n log(n)) |

* #### Time Taken In LeetCode
![](https://i.imgur.com/8zh1ind.png)

* #### The quick sort works on the divide-and-conquer principle. First, it partitions the list of items into two sublists based on a pivot element. All elements in the first sublist are arranged to be smaller than the pivot, while all elements in the second sublist are arranged to be larger than the pivot. The same partitioning and arranging process is performed repeatedly on the resulting sublists until the whole list of items are sorted.

* #### The quick sort is regarded as the best sorting algorithm. This is because of its significant advantage in terms of efficiency because it is able to deal well with a huge list of items. Because it sorts in place, no additional storage is required as well. The slight disadvantage of quick sort is that its worst-case performance is similar to average performances of the bubble, insertion or selections sorts. In general, the quick sort produces the most effective and widely used method of sorting a list of any item size.

### References：
* https://www.youtube.com/watch?v=SLauY6PpjW4&t=300s
* https://www.youtube.com/watch?v=7h1s2SojIRw
* https://www.youtube.com/watch?v=-qOVVRIZzao
* https://www.youtube.com/watch?v=oBXZmAwNFzY
