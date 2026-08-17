class Node:
    def __init__(self,info):
        self.data=info
        self.next=None
class StackLL:
    def __init__(self,head=None):
        self.head=head
    def Insert(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        return
   def peek(self):
        if self.head is None:
            print("Stack is Empty ")
            return
        else:
            print("Top",self.head.data)
