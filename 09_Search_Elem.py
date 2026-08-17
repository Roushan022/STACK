class Stack:
    def __init__(self):
        self.item=[]
    def InsertVal(self,value):
        self.item.append(value)

    def SearchElem(self,item):
        for val in  self.item:
            if item==val:
                print(f"Item is found ")
                return
                
SS=Stack()
Value=input("Enter all the value ").split()
for i in Value:
    SS.InsertVal(int(i))
SS.SearchElem(20)
