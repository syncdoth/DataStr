from DataStr.Node import Node

class Queue:
    def __init__(self):
        self.first = None #front
        self.last = None #back

    def isempty(self):
        if self.first is None:
            return True

        return False

    def front(self):
        if self.isempty():
            return("empty")
        else:
            return(self.first.value)


    def enqueue(self, value):
        new_node = Node(value)
        if self.isempty():
            self.first = new_node
            self.last = new_node
        else:
            n = self.first
            while n.next != None:
                n = n.next
            n.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.isempty():
            print("queue is empty")
            return
        else:
            if self.first == self.last:
                self.first = None
                self.last = None
                return
            self.first = self.first.next

    def __str__(self):
        s = "["
        if self.isempty():
            return('the Queue is empty')
        n = self.first
        while n.next != None:
            s+= str(n.value) + ', '
            n = n.next
        s += str(n.value) + ']'
        return s
