# class HashTable():
#     def __init__(self, length =):


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [None] * 8

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = hash(key) % len(self.array)

        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = hash(key) % len(self.array)

        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = hash(key) % len(self.array)

        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    self.array[index].remove(kvp)
                    break


hashmap = MyHashMap()
hashmap.put(3, 11)
hashmap.put(4, 13)
hashmap.put(15, 6)
hashmap.put(6, 15)
hashmap.put(8, 8)
hashmap.put(11, 0)


print(hashmap.array)
print(hashmap.remove(11))
print(hashmap.get(11))
