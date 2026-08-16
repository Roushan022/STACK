class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.insert(0,value)
        return
    def Size(self):
        if len(self.s)==0:
            raise Exception("The stack is Empty:- ")
            return
        else:
            print(len(self.s))
        return
SS=Stack()
Value=input("Enter all the values to put").split(" ")
for var in Value:
    SS.push(int(var))
SS.Size()
