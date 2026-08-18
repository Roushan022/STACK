class Stack:
    def __init__(self):
        self.s=[]
    def Push(self,value):
        self.s.append(value)
    def RemoveAdj(self):
        i=0
        while(i<len(self.s)-1):
           if(self.s[i]==self.s[i+1]):
                self.s.pop(i)
                self.s.pop(i)
                if i>0:
                    i-=1
           else:
            i+=1
    def Print(self):
        i=0
        while(i< len(self.s)):
            print(self.s[i],end="")
            i+=1
        
SS=Stack()
value=input("Enter the value:- ")
for var in value:
    SS.Push(var)
SS.RemoveAdj()
SS.Print()

