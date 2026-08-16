class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.insert(0,value)
        return    
    def Max(self):
        val=0
        max=self.s[0]
        while val<len(self.s):
            if self.s[val] >max:
                max=self.s[val]
            val+=1

        print(f"Max Elem is the stack is {max}")
        return
SS=Stack()
Value=input("Enter all the values to put").split(" ")
for var in Value:
    SS.push(int(var))
SS.Max()
