# Adjancency matrix
class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_matrix = [[0] * vno for _ in range(vno)]
    
    def add_edge(self,u,v,w=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[v][u]=w
            self.adj_matrix[u][v]=w
        else:
            print("Invalid matrix")
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid matrix")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid matrix")
    
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))

g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)

# g.print_adj_matrix()

# Adjacency list

class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix={v:[] for v in range(vno)}
    
    def add_edge(self,u,v,w=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u].append((v,w))
            self.adj_matrix[v].append((u,w))
        else:
            print("Invalid graph")
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u] = [(vertex,weight) for vertex,weight in self.adj_matrix[u] if vertex!=v]
            self.adj_matrix[v] = [(vertex,weight) for vertex,weight in self.adj_matrix[v] if vertex!=v]
        else:
            print("Invalid graph")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex in self.adj_matrix[u])
        else:
            print("Invalid graph")
    
    def print_adj_list(self):
        for vertex, n in self.adj_matrix.items():
            print("V", vertex, ":", n)

g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)

# g.print_adj_list()