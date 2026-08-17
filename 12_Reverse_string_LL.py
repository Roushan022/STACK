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

    def  Reverse(self):
        t=self.head
        while(t!=None):
            print(t.data,end="")
            t=t.next
        
SS=StackLL()
Value=input("Enter the value ")
for var in Value:
    SS.Insert(var)
SS.Reverse()

        
