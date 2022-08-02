class Hashtable(object):
    def __init__(self, length=4):
        self.array = [None] * length
    
    def hash(self, key):
        length = len(self.array)
        return hash(key) % length
    
    def add(self, key, value):
        index = self.hash(key)
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
    
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for key_val in self.array[index]:
                if key_val[0] == key:
                    return key_val[1]
            
            raise KeyError()

ht = Hashtable()

ht.add(1, "carlos")

print(ht.get(1))
