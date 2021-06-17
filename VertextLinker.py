class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbours = list()
    
    def add_neighbour(self,v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

class Grpah:
    vertices = {}

    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else :
            return False
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices: # To check if vertices are in self.vertices Vertex.
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbour(u)
                if key == v:
                    value.add_neighbour(v)
                return True
            else:
                return False
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours))
                

# Creating a graph
g = Grpah()

a = Vertex('A')
b = Vertex('B')

g.add_vertex(a)
g.add_vertex(b)


for i in range(ord('A'),ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()





