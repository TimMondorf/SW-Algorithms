import random

class Edge:

    def __init__(self, tail, head, weight):
        self.tail = tail
        self.head = head
        self.weight = weight

class Undirected_graph:

    def __init__(self, V):
        self.V = V
        self.vertices = list(range(self.V))
        self.adjacency_list = [ [] for __ in range(self.V) ]
    
    def add_edge(self, new_edge):
        self.adjacency_list[new_edge.head].append(new_edge)
        self.adjacency_list[new_edge.tail].append(new_edge)

class Eager_prim:

    def __init__(self, graph):
        self.graph = graph
        self.marked = self.graph.V * [False]
        self.total_weight = 0
        self.MST = []
        self.q_of_e = []
        self.q_of_e_w = []
        self.source = random.choice(self.graph.vertices)
        self.marked[self.source] = True        
        for x in self.graph.adjacency_list[self.source]:
            self.q_of_e.append(x)
            self.q_of_e_w.append(x.weight)
        while False in self.marked:
            self.min_index = self.q_of_e_w.index(min(self.q_of_e_w))
            self.next_edge = self.q_of_e[self.min_index]
            del self.q_of_e[self.min_index]
            del self.q_of_e_w[self.min_index]
            self.MST.append(self.next_edge)
            self.total_weight += self.next_edge.weight
            if self.marked[self.next_edge.head] == False:
                self.next_vertex = self.next_edge.head
            elif self.marked[self.next_edge.tail] == False:
                self.next_vertex = self.next_edge.tail
            self.marked[self.next_vertex] = True
            for x in self.graph.adjacency_list[self.next_vertex]:
                if self.marked[x.tail] == False or self.marked[x.head] == False:
                    self.q_of_e.append(x)
                    self.q_of_e_w.append(x.weight)
        
        print('The minimum spanning tree for the graph is: ')
        for x in self.MST:
            print(str(x.tail) + ' - ' + str(x.head) + ' . Weight = ' + str(x.weight))
        print('The weight of the MST is ' + str(self.total_weight))
        print('The length of the MST is ' +str(len(self.MST)))
                
tim_graph = Undirected_graph(100)
i = 0
while i < 99:
    edgo = Edge(i, i+1, i * 0.1)
    tim_graph.add_edge(edgo)
    i += 1
tim_graph_find_mst = Eager_prim(tim_graph)

