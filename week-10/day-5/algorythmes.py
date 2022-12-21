class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.lenght = 0
    
    def push(self, data):
        node = Node(data)
        self.lenght= self.lenght+1
        
        if self.head == None:
            self.head = node
            return node

        currItem = self.head
        while (currItem.next != None):
            currItem = currItem.next

        currItem.next = node
     

classPy = LinkedList(None) # {head:None , length:0}
classPy.push("Hadas") # classPy: {head:{data:"hadas" , next:None}}
classPy.push("Daniel") # classPy: {head:{data:"hadas" , next:{data:'daniel', next:none}}}
classPy.push("Elena") # classPy: {head:{data:"hadas" , next:{data:'daniel', next:{data:'elena' , next:none}}}}
classPy.push("Sarah") # classPy: {head:{data:"hadas" , next:{data:'daniel', next:{data:'elena' , next:{data:'Sarah' , next:None}}}}}