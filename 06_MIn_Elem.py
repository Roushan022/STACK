class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.insert(0,value)
        return    
    def Min(self):
        val=0
        min=self.s[0]
        while val <len(self.s):
            if self.s[val] < min:
                min=self.s[val]
            val +=1
        print(f"Min Elem in the Stack is {min}")
        return
SS=Stack()
Value=input("Enter all the values to put").split(" ")
for var in Value:
    SS.push(int(var))
SS.Min()
