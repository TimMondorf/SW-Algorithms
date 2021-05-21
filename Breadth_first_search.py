from queue import Queue
class Graph:

    def __init__(self, V):
        self.V = V
        self.adjacency_list = [ [] for __ in range(V) ] 
    
    def add_edge(self, tail, head):
        self.adjacency_list[tail].append(head)
        self.adjacency_list[head].append(tail)

class BFS:

    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.marked = self.graph.V * [None]
        self.marked[self.source] = True
        self.path = [self.source]
        self.path_to = self.graph.V * [ [] ]
        self.q_of_v = Queue()
        if not len(self.graph.adjacency_list[self.source]) == 0:
            for x in self.graph.adjacency_list[self.source]:
                self.q_of_v.put(x)
        while not self.q_of_v.empty():
            self.next_vertex = self.q_of_v.get()
            self.path.append(self.next_vertex)
            self.marked[self.next_vertex] = True
            self.path_to[self.next_vertex] = self.path.copy()
            if not len(self.graph.adjacency_list[self.next_vertex]) == 0:
                for x in self.graph.adjacency_list[self.next_vertex]:
                    if not self.marked[x] == True:
                        self.q_of_v.put(x)
        
    def is_connected(self, head):
        if self.marked[head] == None:
            return False
        else:
            return True
    
    def show_path(self, head):
        return self.path_to[head]
    
    def degree_of_separation(self, head):
        return len(self.path_to[head]) - 1


tim_graph = Graph(50)

listo =  [0, 10, 20, 30, 40, 49]

for i in range(1, len(listo)):
    tim_graph.add_edge(listo[i-1], listo[i])

tim_search_1 = BFS(tim_graph, 0)
print('Is vertex 10 connected to the source?')
print(tim_search_1.is_connected(10))
print('Is vertex 40 connected to the source?')
print(tim_search_1.is_connected(40))
print('Is vertex 49 connected to the source?')
print(tim_search_1.is_connected(49))
print('How do we get from 0 to 40?')
print(tim_search_1.show_path(40))
print('What is the degree of separation of 0 and 30?')
print(tim_search_1.degree_of_separation(30))
print('Is vertex 27 connected to the source?')
print(tim_search_1.is_connected(27))
tim_search_2 = BFS(tim_graph, 40)
print('Are 40 and 20 connected?')
print(tim_search_2.is_connected(20))
            

