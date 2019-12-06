class Hash:
    def __init__(self, m, R):
        self.size = m
        self.table = [None] * m
        self.state = ['E'] * m # E for Empty, A for active, D for deleted
        self.R = R


    def __key_to_int(self, key):
        l = []
        for c in key:
            l.append(ord(c))
        return l

    def __hf1(self, key): #hash function 1
        L = len(key)
        sum = 0
        key = self.__key_to_int(key)
        for i in range(L):
            sum += (37**(L-1-i))*key[i]

        index = sum % self.size
        return index

    def __hf2(self, key):
        sum = 0
        key = self.__key_to_int(key)
        return self.R - (sum(key) % self.R)


    def __probe(self, key, condition):
        index = self.__hf1(key)
        ohv = index
        i= 0
        while self.table[index] != None:
            if condition == 'i':
                if self.state[index] == 'A':
                    index = (ohv + i**2) % self.size
                    print(index)
                    if index == ohv:
                        return 'error'
                    i += 1
                else:
                    break

            elif condition == 's' or condition == 'd':
                if self.table[index][1] != key or self.state[index] == 'D':
                    index = (ohv + i**2) % self.size
                    if index == ohv:
                        return 'not found'
                    i += 1
                else:
                    break

        return index

    def insert(self, item, key):
        index = self.__probe(key, 'i')
        if index == 'error':
            return index

        self.table[index] = (item, key)
        self.state[index] = 'A'


    def search(self, key):
        index = self.__probe(key,'s')
        if index == 'not found':
            return index

        return self.table[index]


    def delete(self, key):
        index = self.__probe(key,'d')
        if index == 'not found':
            print('item is not in the table')
        else:
            self.state[index] = 'D'

    def __rehash(self):
        return
