from Graph.graph import Graph

class GetImpostors : 
    
    def build_graph(self):
        """
        Function to build the graph of the situation of step 2.
        """
        
        graph = Graph(is_directed=False)
        
        graph.add_edge('Player_0','Player_1')
        graph.add_edge('Player_0','Player_4')
        graph.add_edge('Player_0','Player_5')
        graph.add_edge('Player_1','Player_2')
        graph.add_edge('Player_1','Player_6')
        graph.add_edge('Player_2','Player_3')
        graph.add_edge('Player_2','Player_7')
        graph.add_edge('Player_3','Player_4')
        graph.add_edge('Player_3','Player_8')
        graph.add_edge('Player_4','Player_9')
        graph.add_edge('Player_5','Player_8')
        graph.add_edge('Player_5','Player_7')
        graph.add_edge('Player_6','Player_8')
        graph.add_edge('Player_6','Player_9')
        graph.add_edge('Player_7','Player_9')
        
        return graph
            
    def find_impostors(self,graph, killed_node, set_of_suspects):
        """
        Function to get the list of suspect people to be the second impostor, given the 
        suspected players to be the first impostor. Based on graph coloring theory.

        :param graph : a graph to describe which player met
        :type graph : Graph
        :param killed_node : set of the killed nodes
        :type killed_node : set of Node
        :param set_of_suspects : set of suspected players
        :type set_of_suspects : set of Node 
        """
 
        for n in set_of_suspects:
            non_suspect = [x[0] for x in n.get_adjacents()]
            print('If {} is the first impostor so the suspects are : '.format(n.id))
            res = list(set(graph.nodes.values()) - killed_node - set_of_suspects - set(non_suspect))
            for node in res:
                print(node.id)
            print('\n------------------------\n')

    def run(self):
        """
        Function to run the third step of the project
        """
        print("Let's find the second impostor ")
        print('\n------------------------\n')
        graph = self.build_graph()
        killed = {graph.nodes.get('Player_0')}
        suspects = {graph.nodes.get('Player_1'),graph.nodes.get('Player_4'),graph.nodes.get('Player_5')}
        self.find_impostors(graph = graph , killed_node = killed, set_of_suspects = suspects)