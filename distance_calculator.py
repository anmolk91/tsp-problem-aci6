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

    def read_input(self, input_file_name):
        """
            reads raw file input and convert the raw data to
            edges and vertices
        """
        return self.format_raw_data(self.get_file_content(input_file_name))

    def format_raw_data(self, input_raw_data = ''):
        """
            formats raw input data in to edges and vertices
        """
        data = input_raw_data.split('\n')
        vertices_list = []
        edges_list = []
        prompts = []
        promptObj = {
            'source': -1,
            'pharmacy1': None,
            'pharmacy2': None
        }
        for raw_data_line in data:
            if raw_data_line != None:
                if '/' in raw_data_line:
                    data = [data_item.strip() for data_item in raw_data_line.split('/')]
                    if len(data) == 3:
                        if data[0] not in vertices_list:
                            vertices_list.append(data[0])
                        if data[1] not in vertices_list:
                            vertices_list.append(data[1])
                        new_edge_id = ''.join(sorted(data))
                        if next((edge for edge in edges_list if edge['edge_id'] == new_edge_id ), None) == None:
                            edges_list.append( { 'edge_id': new_edge_id, 'vertice_one': data[0], 'vertice_two': data[1], 'weight': data[2] } )
                elif 'House' in raw_data_line:
                    inp_list = raw_data_line.split(':')
                    promptObj['source'] = inp_list[1].strip()
                elif 'Pharmacy 1' in raw_data_line:
                    inp_list = raw_data_line.split(':')
                    promptObj['pharmacy1'] = inp_list[1].strip()
                elif 'Pharmacy 2' in raw_data_line:
                    inp_list = raw_data_line.split(':')
                    promptObj['pharmacy2'] = inp_list[1].strip()
                    prompts.append(promptObj)
                    promptObj = {
                        'source': -1,
                        'pharmacy1': None,
                        'pharmacy2': None
                    }


        return {
            'vertices': vertices_list,
            'edges': edges_list,
            'prompts': prompts
        }



