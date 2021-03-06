class HashTable(object):
    """ Hash Table """

    def __init__(self, length):
        self.length = length
        self.array = [[] for _ in range(length)]

    def lookup(self, key, default=None):
        """ Look up value from array by its key """
        hash_key = hash(key) % self.length
        bucket = self.array[hash_key]
        if not bucket:
            return default
        for key_val_pair in bucket:
            k, v = key_val_pair
            if k == key:
                return v

    def insert(self, key, value):
        """ Insert a value to array by its key """
        hash_key = hash(key) % self.length
        bucket = self.array[hash_key]
        for idx, key_val_pair in enumerate(bucket):
            k, v = key_val_pair
            if k == key:
                bucket[idx] = [key, value]
                return
        bucket.append([key, value]) 

    def delete(self, key):
        """ Delete a value from array by its key """
        hash_key = hash(key) % self.length
        bucket = self.array[hash_key]
        if not bucket:
            raise ValueError('Key does not exist')
        for key_val_pair in bucket:
            if key_val_pair[0] == key:
                bucket.remove(key_val_pair)

    def update(self, key, value):
        """ Update a value in array by its key """
        hash_key = hash(key) % self.length
        bucket = self.array[hash_key]
        if not bucket:
            raise ValueError('Key does not exist')
        for key_val_pair in bucket:
            if key_val_pair[0] == key:
                key_val_pair[1] = value
                break

if __name__ == "__main__":
    ### driver code
    hash_table = HashTable(length=5)
    hash_table.insert(10, 'USA')
    hash_table.insert(20, 'Canada')
    hash_table.insert(20, 'Mexico')
    hash_table.insert(25, 'Germany')
    hash_table.insert(32, 'France')
    hash_table.delete(20)
    hash_table.update(25, 'Japan')
    print(hash_table.lookup(10))
    print(hash_table.array)