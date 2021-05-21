import random
class Tim_quick_find():

    def __init__(self, N):
        self.array = N * [None]
        self.N = len(self.array)
        for i in range(self.N):
            self.array[i] = i
        #index er site-navne og værdier er ID
    
    def show_array(self):
        return self.array
    
    def find(self, p):
        return self.array[p]
    
    def union(self, p, q): 
        winning_index = self.array[p]
        losing_index = self.array[q]
        for i in range(len(self.array)):
            if self.array[i] == losing_index:
                self.array[i] = winning_index

    def connected(self, p, q):
        if self.array[p] == self.array[q]:
            return True
        else:
            return False

class Tim_quick_union():

    def __init__(self, N):
        self.array = N * [None]
        self.N = len(self.array)
        for i in range(self.N):
            self.array[i] = i
    
    def show_array(self):
        return self.array
    
    def find_root(self, p):
        i = p
        while not self.array[i] == i:
            i = self.array[i]
        return i
    
    def union(self, p, q):
        valg = random.choice([1, 2])
        if valg == 1:
            winning_root = self.find_root(p)
            self.array[self.find_root(q)] = winning_root
        elif valg == 2:
            winning_root = self.find_root(q)
            self.array[self.find_root(p)] = winning_root

    def connected(self, p, q):
        if self.find_root(p) == self.find_root(q):
            return True
        else:
            return False

    
class Tim_weighted_quick_union():

    def __init__(self, N):
        self.array = N * [None]
        self.sz = N * [None]
        self.N = len(self.array)
        for i in range(self.N):
            self.array[i] = i
            self.sz[i] = 1
    
    def show_array(self):
        return self.array
    
    def show_tree_sizes(self):
        return self.sz

    def find_root(self, p):
        i = p
        while not self.array[i] == i:
            i = self.array[i]
        return i

    def find_tree_size_of_node(self, p):
        return self.sz[p]   
    
    def union(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        if self.sz[root_p] >= self.sz[root_q]:
            winning_root = root_p
            losing_root = root_q
        else:
            winning_root = root_q
            losing_root = root_p
        self.array[losing_root] = winning_root
        self.sz[winning_root] += self.sz[losing_root]
             
    def connected(self, p, q):
        if self.find_root(p) == self.find_root(q):
            return True
        else:
            return False

class Tim_weighted_union_with_path_compression():

    def __init__(self, N):
        self.array = N * [None]
        self.sz = N * [None]
        self.N = len(self.array)
        for i in range(self.N):
            self.array[i] = i
            self.sz[i] = 1
    
    def show_array(self):
        return self.array
    
    def show_tree_sizes(self):
        return self.sz

    def find_root(self, p):
        self.find_list = []
        i = p
        while not self.array[i] == i:
            self.find_list.append(i)
            i = self.array[i]
        if not len(self.find_list) == 0:
            for x in self.find_list:
                self.array[x] = i
                self.sz[i] += 1
        return i
             
    def union(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        if self.sz[root_p] >= self.sz[root_q]:
            winning_root = root_p
            losing_root = root_q
        else:
            winning_root = root_q
            losing_root = root_p
        self.array[losing_root] = winning_root
        self.sz[winning_root] += self.sz[losing_root]
                     
    def connected(self, p, q):
        if self.find_root(p) == self.find_root(q):
            return True
        else:
            return False

tim_4 = Tim_weighted_union_with_path_compression(100)
for i in range(50, 60):
    tim_4.union(i, i+1)
for i in range(65, 85):
    tim_4.union(i, i+1)
tim_4.union(55, 75)
print(tim_4.connected(55, 75))
