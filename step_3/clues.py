from Graph.graph import Graph
import pandas as pd

class TimeComparator :

    def floyd_warshall(self,graph):
        """
        Function to get the matrix of shortest path between two nodes using
        Floyd-Warshall algorithme.

        :param graph : the graph to compute th algo on
        :type graph : Graph
        """
        matrix = graph.create_matrix()
        for k in range(graph.nodes_number):
            for i in range(graph.nodes_number):
                for j in range(graph.nodes_number):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        return matrix

    def create_impostor_graph(self):
        """
        Function to build the impostors map with vents.
        """

        impostors_graph = Graph(is_directed=False)

        impostors_graph.add_edge(1,2,0)
        impostors_graph.add_edge(1,3,0)
        impostors_graph.add_edge(1,4,3)
        impostors_graph.add_edge(2,3,5)
        impostors_graph.add_edge(2,4,2)
        impostors_graph.add_edge(2,5,3)
        impostors_graph.add_edge(2,8,5)
        impostors_graph.add_edge(3,4,2)
        impostors_graph.add_edge(3,6,3)
        impostors_graph.add_edge(3,7,5)
        impostors_graph.add_edge(4,5,0)
        impostors_graph.add_edge(4,6,0)
        impostors_graph.add_edge(5,8,2)
        impostors_graph.add_edge(5,6,0)
        impostors_graph.add_edge(6,7,2)
        impostors_graph.add_edge(7,8,5)
        impostors_graph.add_edge(7,11,2)
        impostors_graph.add_edge(7,13,4)
        impostors_graph.add_edge(7,12,2)
        impostors_graph.add_edge(8,11,0)
        impostors_graph.add_edge(8,10,0)
        impostors_graph.add_edge(8,9,3)
        impostors_graph.add_edge(9,10,2)
        impostors_graph.add_edge(9,13,5)
        impostors_graph.add_edge(9,14,0)
        impostors_graph.add_edge(10,11,0)
        impostors_graph.add_edge(10,13,3)
        impostors_graph.add_edge(10,14,4)
        impostors_graph.add_edge(12,13,2)
        impostors_graph.add_edge(13,14,0)

        return impostors_graph

    

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

        return crewmate_graph

    def map_rooms_name(self):
        """
        Function to get a mapping (dict) between the number and the name of the 
        room on the Among Us graph.
        """
    
        return {1:'Reactor', 2: 'Upper Engine', 3:'Lower Engine', 4:'Security',
                5:'Medbay', 6:'Electrical', 7:'Storage', 8:'Cafetaria',
                9:'Weapons', 10:'O2', 11:'Admin', 12:'Communications', 13:'Shields',
                14:'Navigation'}

    def display_floyd_warshall_matrix(self,graph,player_type='impostors'):
        """
        Function to get a nice display with pandas dataframe of the Floyd-Warshall matrix.

        :param graph : the graph to compute th algo on
        :type graph : Graph
        :param player_type : category of the players linked to the graph
        :type player_type : str
        """
        
        matrix = self.floyd_warshall(graph)
        rooms = self.map_rooms_name()
        print(f'Here is the matrix with the sortest time between each room for {player_type}')
        print('\n----------------------------\n')
        print(pd.DataFrame(matrix,columns=rooms.values(),index = rooms.values()))
        print('\n----------------------------\n')

    def run(self):

        impostors_graph = self.create_impostor_graph()
        crewmate_graph = self.create_crewmate_graph()
        self.display_floyd_warshall_matrix(graph= impostors_graph)
        self.display_floyd_warshall_matrix(graph= crewmate_graph, player_type= 'crewmates' )

        