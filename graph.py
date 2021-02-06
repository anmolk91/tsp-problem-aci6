import math

class Graph:

    vertices = []
    edges = []
    adjacency_matrix = []
    distance_matrix = []
    path = []

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_matrix = self.generate_adjacency_matrix(edges)

    def generate_adjacency_matrix(self, edges):
        """
            generates adjacency matrix for the graph
        """
        adjacency_matrix_init = [[0 for i in self.vertices] for j in self.vertices]
        for edge in edges:
            index_one = self.vertices.index(edge['vertice_one'])
            index_two = self.vertices.index(edge['vertice_two'])
            adjacency_matrix_init[index_one][index_two] = int(edge['weight'])
            adjacency_matrix_init[index_two][index_one] = int(edge['weight'])
            
        for i in range(len(self.vertices)):
            index = int(i)
            adjacency_matrix_init[index][index] = math.inf

        return adjacency_matrix_init

    def find_path(self, source_index):
        """
            finds the most efficient path usin A* algorithm
        """
        return self.