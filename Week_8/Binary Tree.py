class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.check = 0

    def checkLen(self):
        return self.size

    def is_Empty(self):
        if self.size <= 0:
            return False
        else:
            return True

    def is_root(self,val):
        if self.size == 0:
            return -1
        return self.root_check(val,self.head)

    def root_check(self,val,current): # Note
        if current == None:
            return
        if current.val == val:
            if (current.left != None) or (current.right != None):
                return True
            else:
                return False
        check = self.root_check(val,current.left)
        check = self.root_check(val,current.right)
        return check

    def is_leaf(self,val):
        if self.size == 0:
            return -1
        return self.leaf_check(val,self.head)

    def leaf_check(self,val,current):
        if current == None:
            return
        if current.val == val:
            if (current.left == None) and (current.right == None):
                return True
            else:
                return False
        self.leaf_check(val,current.left)
        self.leaf_check(val,current.right)
        return

    def depth(self,val):
        if self.size == 0:
            return -1
        self.check = -1
        count = self.depth_check(val,self.head,0)
        if count == -1:
            return -1
        return self.check

    def depth_check(self,val,current,count):
        temp = count
        if current == None:
            return
        if current.val == val:
            self.check = temp
            return
        self.depth_check(val,current.left,temp+=1)
        self.depth_check(val,current.right,temp+=1)
        return

    def height(self):
        if self.size == 0:
            return -1
        self.check = 0
        return self.height_check(self.head,0)

    def height_check(self,current,count):
        temp = count
        if current == None:
            if self.check < temp:
                self.check = temp
        self.height_check(current.left,temp+=1)
        self.height_check(current.right,temp+=1)
        return

    def add_left(self,position,val):
        self.add_left_node(position,val)

    def add_left_node(self,):
