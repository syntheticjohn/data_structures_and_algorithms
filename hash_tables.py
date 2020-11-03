class HashTable(object):
    """ Hash Table """
    def __init__(self, length):
        self.length = length
        self.array = [[] for _ in range(length)]

    def lookup(self, key):
        """ Look up value from array by its key """ 
        hash_key = hash(key) % self.length
        bucket = self.array[hash_key]
        if not self.array[hash_key]:
            raise KeyError() 
        else:
            for idx, key_val_pair in enumerate(bucket):
                k, v = key_val_pair
                if k == key:
                    return v

    def insert(self, key, value):
        """ Insert a value to array by its key """
        hash_key = hash(key) % self.length
        bucket = self.array[hash_key]
        key_exists = False
        for idx, key_val_pair in enumerate(bucket):
            k, v = key_val_pair
            if k == key:
                key_exists = True
                break
        if key_exists:
            bucket[idx] = [key, value]
        else:
            bucket.append([key, value])

    def delete(self, key):   
        """ Delete a value from array by its key """
        hash_key = hash(key) % self.length
        if self.array[hash_key] is None:
            return "Value does not exist at hash_key"
        else:
            for key_val_pair in self.array[hash_key]:
                if key_val_pair[0] == key:
                    self.array[hash_key].remove(key_val_pair)

    def update(self, key, value):
        """ Update a value in array by its key """
        hash_key = hash(key) % self.length
        if self.array[hash_key] is None:
            return "No value to update at hash_key"
        else:
            for key_val_pair in self.array[index]:
                if key_val_pair[0] == key:
                    key_val_pair[1] = value
                    break

if __name__ == "__main__":
    hash_table = HashTable(length=5)
    hash_table.insert(10, 'USA')    
    hash_table.insert(20, 'Canada')
    hash_table.insert(25, 'Germany')
    hash_table.insert(32, 'France')
    hash_table.delete(20)
    hash_table.update(5, 'Japan')
    print(hash_table.array)