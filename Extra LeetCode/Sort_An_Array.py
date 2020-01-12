class Solution:
    def sortArray(self,a):
        self.sortOperator(a,0,len(a)-1)
        return a
        
    def sortOperator(self,a,low,high):
        if low<high:
            splitpoint=self.partition(a,low,high)
            self.sortOperator(a,low,splitpoint-1)
            self.sortOperator(a,splitpoint+1,high)
            
    def partition(self,a,low,high):
        pivot=a[low]
        left=low+1
        right=high
        done=False
        
        while not done:
            while(left <= right and a[left] <= pivot):
                left+=1
                
            while(a[right] >= pivot and right >= left):
                right-=1
                
            if(left>right):
                done=True
            else:
                a[left],a[right]=a[right],a[left]
                
        a[low],a[right]=a[right],a[low]
        return right