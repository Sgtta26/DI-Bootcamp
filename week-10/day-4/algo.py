class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.lenght = 0
    
    def push(self, node):
        self.lenght= self.lenght+1
        
        if self.head == None:
            self.head = node
            return node

        currItem = self.head
        while (currItem.next != None):
            currItem = currItem.next

        currItem.next = node
     

days_of_the_week = LinkedList(None)
n1 = Node("Sun")
days_of_the_week.push(n1)
days_of_the_week.push(Node("Mon"))
days_of_the_week.push(Node("Tue"))
days_of_the_week.push(Node("Wed"))
days_of_the_week.push(Node("Thu"))
