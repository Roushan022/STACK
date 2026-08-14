# other part are in repo 1 of stack 
def pop(self):
        if len(self.s)==0:
            raise Exception("The Stack is Empty ")
            return
        else:
            print(self.s.pop(0))
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
