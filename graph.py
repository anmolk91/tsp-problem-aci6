import math

class Graph:

    vertices = []
    edges = []
    adjacency_list = {}
    path = []

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = self.generate_adjacency_list(edges)
        print(self.adjacency_list)

    def get_neighbors(self, v):
            value = self.adjacency_list[v]
            return value

    def generate_adjacency_list(self,  edges): 
        """
            generates adjacency list for the graph
        """
        adjacency_list = {}
        for vertex in self.vertices:
            for sourceEdge in filter(lambda x: x['source'] == vertex, edges):
                node = (sourceEdge['destination'], sourceEdge['value'])
                if (vertex not in adjacency_list):
                    adjacency_list[vertex] = [node]
                else:
                    adjacency_list[vertex].append(node)
        return adjacency_list

    def find_path(self, start_node, stop_node, h):
        """
            finds the most efficient path usin A* algorithm
        """
        return self.search_using_astar_algo(start_node, stop_node, h)

    def search_using_astar_algo(self, start_node, stop_node, h):
        open_list = set([start_node])
        closed_list = set([])

        # distance_from_source contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        distance_from_source = {}

        distance_from_source[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or (v in distance_from_source and n in distance_from_source and distance_from_source[v] + h[v] < distance_from_source[n] + h[n]):
                    n = v
        
            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    distance_from_source[m] = distance_from_source[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if distance_from_source[m] > distance_from_source[n] + weight:
                        distance_from_source[m] = distance_from_source[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
