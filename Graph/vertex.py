class Node :
    """
    Class to represent a graph vertex
    """
    def __init__(self, id):
        self.id = id
        self.neighbors = {}
        self.visited = False
        
    def add_adjacent(self,node,weight=1):
        """
        Function to add a new adjacent node (neighbor) to the current node.

        :param node : the new node
        :type node : Node
        :param weight : the cost of the edge between the two nodes
        :type weight : int
        """
        self.neighbors[node] = weight
    
    def get_adjacents(self):
        """
        Function to get all the adjacent node of the current one.
        We return a list of tuple which contains (adjacent_node, weight)
        """
        return [(adj,adj_weight) for adj,adj_weight in self.neighbors.items()]
    
    def get_weight(self,node):
        """
        Function to get the cost of an edge with an adjacent node.

        :param node : the adjacent node
        :type node: Node
        """
        return self.neighbors[node]
    
    def set_visited(self):
        """
        Function to set the current node as "visited". Useful for traversal algorithme.
        """
        self.visited = True
    
    def set_unvisited(self):
        """
        Function to set the current node as "unvisited". Useful for traversal algorithme.
        """
        self.visited = False