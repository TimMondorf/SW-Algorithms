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

class Edge:
    def __init__(self, tail, head, weight):
        self.tail = tail
        self.head = head
        self.weight = weight

class Undirected_graph:
    
    def __init__(self, V):
        self.V = V
        self.adjacency_list = [ [] for __ in range(self.V) ]
        self.edges = []
        self.edge_weights = []
    
    def add_edge(self, new_edge):
        self.adjacency_list[new_edge.tail].append(new_edge)
        self.adjacency_list[new_edge.head].append(new_edge)
        self.edges.append(new_edge)
        self.edge_weights.append(new_edge.weight)

class Kruskal:

    def __init__(self, graph):
        self.graph = graph
        self.sorted_edge_list = []
        self.sorted_edge_weight_list = []
        self.MST_UF = Tim_weighted_quick_union(self.graph.V)
        self.MST_list = []
        self.total_weight = 0
    
        while len(self.graph.edges) > 0:
            self.min_index = self.graph.edge_weights.index(min(self.graph.edge_weights))
            self.sorted_edge_list.append(self.graph.edges[self.min_index])
            self.sorted_edge_weight_list.append(self.graph.edge_weights[self.min_index])
            del self.graph.edges[self.min_index]
            del self.graph.edge_weights[self.min_index]

        for possible_next_edge in self.sorted_edge_list:
            if not self.MST_UF.connected(possible_next_edge.tail, possible_next_edge.head):
                self.MST_UF.union(possible_next_edge.tail, possible_next_edge.head)
                self.MST_list.append(possible_next_edge)
                self.total_weight += possible_next_edge.weight

        print('The minimum spanning tree for the graph is: ')
        for x in self.MST_list:
            print(str(x.tail) + ' - ' + str(x.head) + ' . Weight = ' + str(x.weight))
        print('The weight of the MST is ' + str(self.total_weight))
        print('The length of the MST is ' +str(len(self.MST_list)))


tim_graph = Undirected_graph(100)
i = 0
while i < 99:
    edgo = Edge(i, i+1, i * 0.1)
    tim_graph.add_edge(edgo)
    i += 1
tim_graph_find_mst = Kruskal(tim_graph)

