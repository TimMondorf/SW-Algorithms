class Graph:

    def __init__(self, V):
        self.V = V
        self.adjacency_list = [ [] for __ in range(V) ] 
    
    def add_edge(self, tail, head):
        self.adjacency_list[tail].append(head)
        self.adjacency_list[head].append(tail)

class DFS:

    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.marked = self.graph.V * [None]
        self.path_to = self.graph.V * [None]
        self.marked[source] = True
        self.current_vertex = source
        self.path = []
        while True:
            self.unmarked_found = False
            for x in self.graph.adjacency_list[self.current_vertex]:
                if not self.marked[x] == True:
                    self.unmarked_found = True
                    self.next_vertex = x
                    self.marked[self.next_vertex] = True
                    self.path.append(self.current_vertex)
                    self.path_to[self.current_vertex] = self.path.copy()
                    self.current_vertex = self.next_vertex
                    break
            if not self.unmarked_found:
                if len(self.path) == 0:
                    break
                else:
                    self.current_vertex = self.path.pop()

    def is_connected(self, head):
        if self.marked[head] == None:
            return False
        else:
            return True
    
    def show_path(self, head):
        return self.path_to[head]
#        output_list = []
#        for x in self.path_to[head]:
#            output_list.append(x)
#        return output_list

tim_graph = Graph(50)

listo =  [0, 10, 20, 30, 40, 49]

for i in range(1, len(listo)):
    tim_graph.add_edge(listo[i-1], listo[i])

tim_search_1 = DFS(tim_graph, 0)
print('Is vertex 10 connected to the source?')
print(tim_search_1.is_connected(10))
print('Is vertex 40 connected to the source?')
print(tim_search_1.is_connected(40))
print('Is vertex 49 connected to the source?')
print(tim_search_1.is_connected(49))
print('How do we get from 0 to 40?')
print(tim_search_1.show_path(40))
print('Is vertex 27 connected to the source?')
print(tim_search_1.is_connected(27))
tim_search_2 = DFS(tim_graph, 40)
print('Are 40 and 20 connected?')
print(tim_search_2.is_connected(20))