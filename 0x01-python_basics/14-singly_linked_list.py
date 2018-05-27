#!/usr/bin/python3


class Node:
    """
    node definition
    """
    def __init__(self, data, next_node=None):
        """
        node definition
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        for node data
        """
        return self.__data

    @property
    def next_node(self):
        """
        getter for next_node
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        setter
        """
        if value.__class__ is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        setter
        """
        if value is None or type(value) is Node:
           self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    class definition
    """
    def __init__(self):
        """
        initialization
        """
        self.__head = None

    def __str__(self):
        """
        returns the node data list
        """
        nodeList = []
        n = self.__head
        while n is not None:
            nodeList.append(str(n.data))
            n = n.next_node
        return '\n'.join(nodeList)

    def sorted_insert(self, value):
        """
        inserts a node to list in ascending order
        """
        if self.__head is None or self.__head.data >= value:
            self.__head = Node(value, next_node=self.__head)
        else:
            walk = self.__head
            while walk.next_node and walk.next_node.data < value:
                walk = walk.next_node
            newNode = Node(value, next_node=walk.next_node)
            walk.next_node = newNode
