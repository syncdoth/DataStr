from DataStr.Node import Node

class Stack:
    def __init__(self):
        self.top_node = None
        self.bot_node = None

    def isempty(self):
        if self.bot_node == None:
            return True

        return False

    def push(self, value):
        new_node = Node(value)
        if self.isempty():
            self.top_node = new_node
            self.bot_node = new_node
            return
        else:
            n = self.bot_node
            while n.next != None:
                n = n.next
            n.next = new_node
            self.top_node = new_node

    def pop(self):
        if self.isempty():
            print('the stack is empty')
            return

        n = self.bot_node
        if n == self.top_node:
            self.top_node = None
            self.bot_node = None
            return
        while n.next != self.top_node:
            n = n.next
        n.next = None
        self.top_node = n

    def top(self):
        if self.isempty():
            return "empty"
        return self.top_node.value

    def __str__(self):
        s = "["
        if self.isempty():
            return('the stack is empty')
        n = self.bot_node
        while n.next != None:
            s+= str(n.value) + ', '
            n = n.next
        s += str(n.value) + ']'
        return s
