class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.insert(0,value)
        return    
    def Reverse(self):
        value=[]
        # self.s.reverse()
        # print(self.s)
        for item in self.s:
            print(item,end=" ")
SS=Stack()
Value=input("Enter all the values to put").split(" ")
for var in Value:
    SS.push(int(var))
SS.Reverse()

