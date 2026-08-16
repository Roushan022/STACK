class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.insert(0,value) # insert at 0
        return    
    def Middle(self):
        mid=round(len(self.s)//2)
        print(self.s.pop(mid))
        print(self.s[mid]) # see insertion type
SS=Stack()
Value=input("Enter all the values to put").split(" ")
for var in Value:
    SS.push(int(var))
SS.Middle()
