class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.insert(0,value)    # insert elem in the index value zero and push other upside 1,2,3,4
        return
    def peek(self):
        if len(self.s)==0:
            raise Exception("The Stack is Empty ")   
            return
        else:
            print(self.s[0])

    
