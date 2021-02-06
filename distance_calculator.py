from graph import Graph

class DistanceCalculator :

    edges = []
    vertices = []
    distanceGraph = None

    def __init__(self, file_name):
        data = self.collect_input()

        self.distanceGraph = Graph(data['vertices'], data['edges'])
        self.distanceGraph.find_path(data['source'], data['destination'], data['h_val'])

    def collect_input(self): 
        vertices_count = int(input('Enter the no of vertices in the graph = '))
        vertices = []
        for index in range(vertices_count):
            vertices.append(input('Enter vertex = ').strip())

        edges_count = int(input('Enter the no of edges = '))
        edges = []
        for index in range(edges_count):
            edge = input('Enter edge (S / D / V where S = Source, D = Destination, V = Value) ')
            details = edge.split('/')
            edges.append({
                'source': details[0].strip(),
                'destination': details[1].strip(),
                'value': float(details[2].strip())
            })
        h_val = {}
        for vertex in vertices:
            h_val[vertex] = float(input('Enter heuristic value for ' + vertex + ' '))

        source_node = input('Enter Source node ')
        destination_node = input('Enter Destination node')

        return {
            'vertices': vertices,
            'edges': edges,
            'h_val': h_val,
            'source': source_node,
            'destination': destination_node
        }


