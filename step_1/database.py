# -*- coding: utf-8 -*-
import sys
from .player import Player

class AVLTree:
    
    def __init__(self,root=None):
        self.root = root
        self.nodes_number = 1 if root else 0
        
    def insert_node(self, root, new_node,avl):
        """
        This function allows us to add a new node to the tree and update the nodes number.
        We also rebalence the tree after adding the node. 

        :param root: top node of our tree.
        :type root: Player (node)
        :param new_node: the node to add to the tree.
        :type new_node : Player (node)
        :param avl : it's the AVL instance in wich we will add the node. Useful to update nodes number.
        :type avl : AVLTree
        """

        # Search for the location to add the new node
        if root is None:
            root = new_node
            avl.update_nb()
        elif new_node.value < root.value:
            root.left = self.insert_node(root.left, new_node,avl)
        else:
            root.right = self.insert_node(root.right, new_node,avl)
        
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        
        # Update the balance factor 
        balance_factor = self.get_balance(root)
        
        # Balance the tree
        if balance_factor > 1:
            if new_node.value <= root.left.value:
                root= self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                root =  self.right_rotation(root)

        if  balance_factor < -1:
            if new_node.value >= root.right.value:
                root = self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)

        return root
    
    def delete_node(self,root,node,avl):
        """
        This function allows us to remove a node from the tree and update the nodes number.
        We also rebalence the tree after adding the node. 

        :param root: top node of our tree.
        :type root: Player (node)
        :param new_node: the node to remove from the tree.
        :type new_node : Player (node)
        :param avl : it's the AVL instance in wich we will add the node. Useful to update nodes number.
        :type avl : AVLTree
        """
        if root is None:
            return root
        # Searching the node by it's name
        else:
            if root.id == node.id:
                
                # case where node is a leaf
                if root.left is None and root.right is None:
                    root = None
                # case where node has one child
                elif root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
                # case where node has two childs
                else : 
                    temp = self.get_min_value_node(root.right)
                    root.value = temp.value
                    root.right = self.delete_node(root.right,temp,avl)
                
                avl.update_nb(add=False)
                return root
            
            elif root.value < node.value :
                root.right = self.delete_node(root.right,node,avl)
            else :
                root.left = self.delete_node(root.left,node,avl)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance_factor = self.get_balance(root)

        # Balance the tree
        if balance_factor > 1:
            if self.get_balance(root.left) >= 0:
                root = self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                root = self.right_rotation(root)
        if balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                root = self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)
        return root

    def update_nb(self,add=True):
        """
        This function is here to update the nodes number after adding or deleting node.

        :param add : it tell us if we are adding or not (deleting)
        :type add : bool
        """
        if add:
            self.nodes_number = self.nodes_number + 1
        else : 
            self.nodes_number = self.nodes_number - 1 
       
    def left_rotation(self, node):
        """
        This function perform a left rotation on a node

        :param node : node to perform the rotation on
        :type node : Player (node)
        """
        old_right = node.right
        old_left = old_right.left
        old_right.left = node
        node.right = old_left
        
        # Update the balance factor of nodes
        node.height = 1 + max(self.get_height(node.left),
                           self.get_height(node.right))
        old_right.height = 1 + max(self.get_height(old_right.left),
                           self.get_height(old_right.right))
        return old_right

    def right_rotation(self, node):
        """
        This function perform a right rotation on a node

        :param node : node to perform the rotation on
        :type node : Player (node)
        """
        old_left = node.left
        old_right = old_left.right
        old_left.right = node
        node.left = old_right

        # Update the balance factor of nodes
        node.height = 1 + max(self.get_height(node.left),
                           self.get_height(node.right))
        old_left.height = 1 + max(self.get_height(old_left.left),
                           self.get_height(old_left.right))
        return old_left

    def get_height(self, root):
        """ 
        This function return the height of a node

        :param root : the concerned node
        :type root : Player (node)
        """
        
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def get_balance(self, root):
        """ 
        This function return the balance of a node

        :param root : the concerned node
        :type root : Player (node)
        """

        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        """
        This function return the node with the lowest value in the tree

        :param root : root node of the tree
        :type root : Player (node) 
        """
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def get_max_value_node(self, root):
        """
        This function return the node with the highest value in the tree

        :param root : root node of the tree
        :type root : Player (node) 
        """
        if root is None or root.right is None:
            return root
        return self.get_max_value_node(root.right)
        
    def printHelper(self, currPtr, indent, last):
        #print('Start')
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(f'{currPtr.id},{currPtr.value}')
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

    def inorder(self,root):
        """
        This function return the list of all nodes by an inorder traversal (sorted by value)

        :param root : root node of the tree
        :type root : Player (node) 
        """
        if root==None:
            return []

        left_list = self.inorder(root.left)
        right_list = self.inorder(root.right)
        return left_list + [root] + right_list 