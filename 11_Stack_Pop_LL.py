def pop(self):
        if self.head is None:
            print("Stack is empty ")
            return
        value=self.head.data
        print("Elemnt Deleted :-  ",value)
        self.head=self.head.next
        return
  
