
class Vertex:
    def __init__(self, n):
        self.name = n
        self.edges = list()


class Edges:
    def __init__(self, vertex):
        self.destinationVertex = vertex


def read_input(fromPath):
    with open(fromPath) as f:
        lines = f.readlines()[0]
        return lines.rsplit('=', 1)[1]


class Graph:

    def __init__(self):
        self.vertices = list()

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edges(self, vertex_one, vertex_two):
        return vertex_one.edges.append(Edges(vertex_two))  # Since graph is one directional

    def print_graph(self,input_airport):
        input_airport_vertex = list(filter(lambda vertex: vertex.name == input_airport, self.vertices))[0]
        print(f'Airport Name is {input_airport_vertex.name}')
        for each in self.vertices:
            print(f'Input airport {each.name} == connections {len(each.edges)}')
            for vertex in each.edges:
                print(vertex.destinationVertex.name)




        # empty_array = np.empty((0, 2), str)
        # for each_edge in get_edges:
        #     reader = each_edge.rsplit(',')
        #     empty_array = np.append(empty_array, np.array([[reader[0], reader[1]]]), axis=0)
        # print(empty_array)


# input_flight = read_input('/Users/sraavanchevireddy/Downloads/Input.txt')
inputFlight = "DEL"
list_of_airports = {'BGI', 'CDG', 'DEL', 'DOH', 'DSM', 'EWR', 'EYW', 'HND', 'ICN', 'JFK', 'LGA', 'LHR', 'ORD', 'SAN',
                    'SFO', 'SIN', 'TLV', 'BUD'}

edges = [
    "DSM,ORD",
    "ORD,BGI",
    'BGI,LGA',
    'SIN,CDG',
    'CDG,SIN',
    'CDG,BUD',
    'DEL,DOH',
    'DEL,CDG',
    'TLV,DEL',
    'EWR,HND',
    'HND,ICN',
    'HND,JFK',
    'ICN,JFK',
    'JFK,LGA',
    'EYW,LHR',
    'LHR,SFO',
    'SFO,SAN',
    'SFO,DSM',
    'SAN,EYW']
# Building a graph
g = Graph()


# Adding Vertices.
for each_airport in list_of_airports:
    g.add_vertex(Vertex(each_airport))

#Matching the edges
for each_Edge in edges:
    reader = each_Edge.rsplit(',')
    nodeOne = list(filter(lambda vertex: vertex.name == reader[0], g.vertices))
    nodeTwo = list(filter(lambda vertex: vertex.name == reader[1], g.vertices))
    starting_airport = nodeOne[0]
    destination_airport = nodeTwo[0]
    g.add_edges(starting_airport,destination_airport)

g.print_graph(inputFlight)








#
# g.add_edges(edges)
#
# # Printing Graph
# g.print_graph()
