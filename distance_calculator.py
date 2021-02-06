from graph import Graph

class DistanceCalculator :

    edges = []
    vertices = []
    distanceGraph = None

    def __init__(self, file_name):
        
        data = self.read_input('inputACI6.txt')
        self.distanceGraph = Graph(data['vertices'], data['edges'])
        self.distanceGraph.find_path('A', 'G', data['h_val'])

    def read_input(self, input_file_name):
        """
            reads raw file input and convert the raw data to
            edges and vertices
        """
        return self.format_raw_data(self.get_file_content(input_file_name))

    def get_file_content(self, filePath, mode='r'):
        """
            opens file in the mode provided and returns of the file
        """
        with open(filePath, mode) as my_file:
            return my_file.read()

    def format_raw_data(self, input_raw_data = ''):
        """
            formats raw input data in to edges and vertices
        """
        vertices = []
        edges = []
        h_val = {}
        for rawData in filter(lambda x: x != '', input_raw_data.split('\n')):
            if ',' in rawData:
                for vertex in rawData.split(','):
                    vertices.append(vertex.strip())
            elif rawData.count('/') == 2:
                edgeData = rawData.split('/')
                edges.append({
                    'source': edgeData[0].strip(),
                    'destination': edgeData[1].strip(),
                    'value': float(edgeData[2].strip())
                })
            elif rawData.count('/') == 1:
                h_details = rawData.split('/')
                if h_details[0].strip() not in  h_val:
                    h_val[h_details[0].strip()] = float(h_details[1])
        return {
            'vertices': vertices,
            'edges': edges,
            'h_val': h_val
        }

