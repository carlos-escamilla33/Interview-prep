class Hashtable(object):
    def __init__(self, length=4):
        # Initiate our array with empty values.
        self.array = [None] * length
    
    def hash(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length
    
    def add(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)
        if self.array[index] is not None:
            # This index already cnotains some values.
            # This means that this add MIGHT be an update
            # to a key that already exists. Instead of just storing
            # the value we have to first look if the key exists.
            for keyValPair in self.array[index]:
                # If key is found, then update
                # its current value to the new value
                if keyValPair[0] == key:
                    keyValPair[1] = value
                    break
                else:
                    # If no breaks was hit in the for loop, it
                    # means that no existing key was found,
                    # so we can simply just add it to the end
                    self.array[index].append([key, value])
        else:
            # This index is empty. We should initialize
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])
    
    def get(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exists. If it does
            # then return its value
            for keyValPair in self.array[index]:
                if keyValPair[0] == key:
                    return keyValPair[1]
            
            # If no return was done during the loop
            # it means key didnt exist
            raise KeyError()

ht = Hashtable()
ht.add("carlos", "escamilla")

print(ht.get("carlos"))