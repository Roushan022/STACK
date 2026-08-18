class Node:
    def __init__(self,info):
        self.data=info
        self.next=None
class StackLL():
    def __init__(self,head=None):
        self.head=head
    def Insert(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp
        return
    def Palind_check(self):
        t=self.head
        check=""
        while(t!=None):
            check +=t.data
            t=t.next
        if check==Lower_value:
            print(" palindrome")
            return
        else:
            print(" Not palindorme ")

SL=StackLL()
value=input("Enter a string ")
Lower_value=value.lower()
for var in Lower_value:
    SL.Insert(var)
SL.Palind_check()




