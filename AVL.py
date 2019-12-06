class AVLNode:
    def __init__(self, value = 0):
        self.data = value
        self.left = AVL()
        self.right = AVL()

class AVL:
    def __init__(self):
        self.root = None

    def height(self):

        return

    def bfactor(self):
        return

    def fix_height(self):
        return

    def rotate_left(self):
        return
    def rotate_right(self):
        return
    def balance(self):
        return


    def isempty(self):
        if self.root is None:
            return True
        return False

    def contains(self, x):
        if self.isempty():
            return False
        if self.root.data == x:
            return True

        if self.root.data > x:
            return self.root.left.contains(x)
        if self.root.data < x:
            return self.root.right.contains(x)


    def find_min(self):
        if self.isempty():
            print('empty')
            return
        else:
            n = self.root
            while not n.left.isempty():
                n = n.left.root

            return n.data

    def find_max(self):
        if self.isempty():
            print('empty')
            return
        else:
            n = self.root
            while not n.right.isempty():
                n = n.right.root

            return n.data

    def output(self, depth = 0):

        if self.isempty():
            return

        self.root.right.output(depth+1)
        for i in range(depth):
            print('\t', end = '')
        print(str(self.root.data))
        self.root.left.output(depth+1)

    def insert(self, x):
        if self.isempty():
            self.root = BSTNode(x)

        elif self.root.data > x:
            self.root.left.insert(x)

        elif self.root.data < x:
            self.root.right.insert(x)

    def remove(self,x):
        if self.isempty():
            return

        if self.root.data > x:
            self.root.left.remove(x)
        elif self.root.data < x:
            self.root.right.remove(x)

        elif not self.root.left.isempty() and not self.root.right.isempty():
            self.root.data = self.root.left.find_max()
            self.root.left.remove(self.root.data)

        else:
            if self.root.left.isempty():
                self.root = self.root.right.root
            else:
                self.root = self.root.left.root
