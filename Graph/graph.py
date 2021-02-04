# -*- coding: utf-8 -*-
import math
from Graph.vertex import Node

class Graph:
    """
    Class of a graph represented by an adjacency dictionary.
    """
    
    def __init__(self,is_directed = True):
        self.nodes = {}
        self.nodes_number = 0
        self.is_directed = is_directed
        
    def __iter__(self):
        return iter(self.nodes.values())
    
    def add_node(self,node):
        """
        Function to add a new vertex to our graph.

        :param node: value of the new node
        :type node : int
        """
        self.nodes_number += 1
        new_node = Node(node)
        self.nodes[node] = new_node
        
    def add_edge(self,start,end,weight=1):
        """
        Function to connect two nodes of the graph. 

        :param start : value of the first vertex
        :type start : int
        :param end : value of the second vertex
        :type end : int
        :param weight : distance between the two verteces
        :type weight : int
        """
        if start not in self.nodes:
            self.add_node(start)
        if end not in self.nodes:
            self.add_node(end)
        if self.is_directed:
            self.nodes[start].add_adjacent(self.nodes[end],weight)
        else:
            self.nodes[start].add_adjacent(self.nodes[end],weight)
            self.nodes[end].add_adjacent(self.nodes[start],weight)
    
    def get_node(self,node):
        """
        Function to return the vertex of the given name.

        :param node : name of the vertex to return
        :type node : 
        """
        return self.nodes.get(node,None)
    
    def get_edge_weight(self,u,v):
        """
        Function to get the weight of an edge between two connected verteces

        :param u: name of the first vertex of the edge
        :type u : int
        :param : name of the second vertex of the edge
        :type v : int
        """
        _from = self.nodes.get(u)
        _to = self.nodes.get(v)
        return _from.neighbors.get(_to)
    
    def get_edges(self):
        """
        Function to get a list of all the edges of the graph.
        List element are tuple like (u,v,weight).
        """
        edges = [] 
        for node in self.nodes.values():
            for adj in node.get_adjacents():
                edges.append((node,) + adj)
        return edges

    def create_matrix(self):
        """
        Function to return a adjacency matrix of the graph.
        It's a list of list.
        """
        matrix = []
        for i in range(self.nodes_number):
            new_line = []
            for j in range(self.nodes_number):
                if i ==j:
                    new_line.append(0)
                else:
                    new_line.append(math.inf)
            matrix.append(new_line)
        edges = self.get_edges()
        for edge in edges:
            row = edge[0].id - 1
            col = edge[1].id - 1
            value = edge[2]
            matrix[row][col] = value
        return matrix