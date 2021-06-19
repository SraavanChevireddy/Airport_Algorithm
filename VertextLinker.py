class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbours = list()

    def add_neighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            # self.neighbours.sort() Sorting not required for air travel flow


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        for key, value in self.vertices.items():
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


def read_input(fromPath):
    with open(fromPath) as f:
        lines = f.readlines()[0]
        return lines.rsplit('=', 1)[1]


input_flight = read_input('/Users/sraavanchevireddy/Downloads/Input.txt')
edges = ['DSM, ORD',
         'ORD, BGI',
         'BGI, LGA',
         'SIN, CDG',
         'CDG, SIN',
         'CDG, BUD',
         'DEL, DOH',
         'DEL, CDG',
         'TLV, DEL',
         'EWR, HND',
         'HND, ICN',
         'HND, JFK',
         'ICN, JFK',
         'JFK, LGA',
         'EYW, LHR',
         'LHR, SFO',
         'SFO, SAN',
         'SFO, DSM',
         'SAN, EYW']

# Building a graph
g = Graph()

g.add_vertex(Vertex('BGI'))
g.add_vertex(Vertex('CDG'))
g.add_vertex(Vertex('DEL'))
g.add_vertex(Vertex('DOH'))
g.add_vertex(Vertex('DSM'))
g.add_vertex(Vertex('EWR'))
g.add_vertex(Vertex('EYW'))
g.add_vertex(Vertex('HND'))
g.add_vertex(Vertex('ICN'))
g.add_vertex(Vertex('JFK'))
g.add_vertex(Vertex('LGA'))
g.add_vertex(Vertex('LHR'))
g.add_vertex(Vertex('ORD'))
g.add_vertex(Vertex('SAN'))
g.add_vertex(Vertex('SFO'))
g.add_vertex(Vertex('SIN'))
g.add_vertex(Vertex('TLV'))
g.add_vertex(Vertex('BUD'))

for edge in edges:
    edge_list = edge.rsplit(',')
    g.add_edge(edge_list[0], edge_list[1])

g.print_graph()
