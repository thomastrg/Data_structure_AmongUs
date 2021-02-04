from Graph.graph import Graph

class EndTask : 

    def __init__(self,graph = None):
        
        self.graph = graph

    def create_crewmate_graph(self):
        """
        Function to create the crewmate graph.
        """
        crewmate_graph = Graph(is_directed=False)

        crewmate_graph.add_edge(1,2,3)
        crewmate_graph.add_edge(1,3,3)
        crewmate_graph.add_edge(1,4,3)
        crewmate_graph.add_edge(2,3,5)
        crewmate_graph.add_edge(2,4,2)
        crewmate_graph.add_edge(2,5,3)
        crewmate_graph.add_edge(2,8,5)
        crewmate_graph.add_edge(3,4,2)
        crewmate_graph.add_edge(3,6,3)
        crewmate_graph.add_edge(3,7,5)
        crewmate_graph.add_edge(5,8,2)
        crewmate_graph.add_edge(6,7,2)
        crewmate_graph.add_edge(7,8,5)
        crewmate_graph.add_edge(7,11,2)
        crewmate_graph.add_edge(7,13,4)
        crewmate_graph.add_edge(7,12,2)
        crewmate_graph.add_edge(8,11,3)
        crewmate_graph.add_edge(8,9,3)
        crewmate_graph.add_edge(9,10,2)
        crewmate_graph.add_edge(9,13,5)
        crewmate_graph.add_edge(9,14,3)
        crewmate_graph.add_edge(10,13,3)
        crewmate_graph.add_edge(10,14,4)
        crewmate_graph.add_edge(12,13,2)
        crewmate_graph.add_edge(13,14,4)

        self.graph = crewmate_graph

        
    def hamilton_backtracking(self,path,vertex,all):
        """
        Recursive function to get all possible hamiltonian path from a given vertex.

        :param path : liste of nodes which are in the current path
        :type path : list of int
        :param vertex : the vertex to start the path from
        :type vertex : Node
        :param all : list of all the possible hamiltonian path
        :type all : list of int
        """
        if len(path) == self.graph.nodes_number:
            tmp = path[:]
            all.append(tmp)
            return

        for adj in vertex.neighbors.keys():
            if not adj.visited:
                adj.set_visited()
                path.append(adj.id)
                self.hamilton_backtracking(path,adj,all)
                adj.set_unvisited()
                path.remove(adj.id)

    def hamilton(self):
        """
        Function to compute a hamiltonian algorithme on the crewmate graph, using backtracking
        """
        self.create_crewmate_graph()
        paths = []
        mypath = []
        for v in self.graph.nodes.keys():
            mypath = []
            start = self.graph.get_node(v)
            start.set_visited()
            mypath.append(start.id)
            self.hamilton_backtracking(mypath,start,paths)
            start.set_unvisited()
          
        return paths

    def compute_distance(self,path):
        """
        Function to get the time to go throught all the verteces in the path.

        :param path : the path to folow to go throught all the verteces
        :type path : list of int
        """
        edges = []
        for i in range(len(path) - 1) : 
            edge = (path[i],path[i+1])
            edges.append(edge)
        return sum([self.graph.get_edge_weight(u,v) for u,v in edges])
        

    def map_rooms_name(self):
        """
        Function to get a mapping (dict) between the number and the name of the 
        room on the Among Us graph.
        """
    
        return {1:'Reactor', 2: 'Upper Engine', 3:'Lower Engine', 4:'Security',
                5:'Medbay', 6:'Electrical', 7:'Storage', 8:'Cafetaria',
                9:'Weapons', 10:'O2', 11:'Admin', 12:'Communications', 13:'Shields',
                14:'Navigation'}

    def get_fastest_path(self):
        """
        unction to compute a hamiltonian algorithme on the crewmate graph, and return the fastest one.
        """
        finalpath = self.hamilton() # get all the paths
        paths = [(path,self.compute_distance(path)) for path in finalpath]
        paths = sorted(paths,key=lambda x: x[1]) # sort the path by them cost
        return paths[0][0]

    def map_path_room_name(self,path):
        """
        Function to get associted list of room names of a given path.

        :param path : the path to map the names
        :type path : list of int
        """
        return [self.map_rooms_name().get(room) for room in path]

    def run(self):
        path = self.get_fastest_path()
        final_path = self.map_path_room_name(path)
        print('The Shortest Path is : ')
        print('\n--------------------------------\n')
        for i in range(len(final_path)):
            if i == len(final_path )- 1:
                print(final_path[i])
            else:
                print(final_path[i], end= ' -> ')
        print('\n--------------------------------\n')

