
class Hashtable(object):
    def __init__(self, length=4):
        self.array = [None] * length
    
    def _getHash(self, key):
        length = len(self.array)
        hash = 0
        for char in str(key):
            hash+=ord(char)
        return hash % length
    
    def add(self, key, value):
        index = self._getHash(key)
        if self.array[index] is not None:
            for key_val in self.array[index]:
                if key_val[0] == key:
                    key_val[1] = value
                    break
                else:
                    self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])
            
        if self.is_full():
            self.double()
    
    def get(self, key):
        index = self._getHash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for key_val in self.array[index]:
                if key_val[0] == key:
                    return key_val[1]
            
            raise KeyError()

    def is_full(self):
        items = 0
        for item in self.array:
            if item is not None:
                items+=1
        return items > len(self.array) / 2

    def double(self):
        ht2 = Hashtable(length=len(self.array) * 2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for key_val in self.array[i]:
                ht2.add(key_val[0], key_val[1])
        
        self.array = ht2.array

ht = Hashtable()

ht.add(1, "carlos")

print(ht.is_full())
