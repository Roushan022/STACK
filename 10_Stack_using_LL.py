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
SS=StackLL()
SS.Insert(20)
SS.Insert(30)
SS.Insert(50)
