class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
    
class Table():

    def __init__(self, hash_value):
        self.hash_value = hash_value
        self.array = self.hash_value * [ [] ]
    
    def insert(self, node):
        self.array[self.hash_function(node.key)].append(node)
    
    def find(self, key):
        for x in self.array[self.hash_function(key)]:
            if x.key == key:
                return x.value
    
    def hash_function(self, key):
        return key % self.hash_value

import string
alfa = string.ascii_lowercase

tim_table = Table(5)

for x in alfa:
    new_node = Node(alfa.index(x), x)
    tim_table.insert(new_node)

for i in range(26):
    print(tim_table.find(i))