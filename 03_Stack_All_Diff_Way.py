class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.append(value)
        return
    def peek(self):
        if len(self.s)==0:
            raise Exception("The Stack is Empty ")
            return
        else:
            print(self.s[-1])
    def pop(self):
        if len(self.s)==0:
            raise Exception("The Stack is Empty ")
            return
        else:
            print(self.s.pop(-1))
            return
    def Length(self):
        print(len(self.s))
        return
    
Stk=Stack()
Stk.push(89)
Stk.push(78)
Stk.push(34)
Stk.push(67)
Stk.push(90)
Stk.Length()
Stk.pop()
Stk.peek()
Stk.pop()
Stk.peek()
Stk.Length()

