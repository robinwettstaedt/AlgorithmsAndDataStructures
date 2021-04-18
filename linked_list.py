#!/usr/bin/env python
"""
This module provides the functionality of a Linked List.

Following along with a Course on Algorithms and Datastructures, this module shares similarity
with the coding examples shown in said course. The code was still written by me and there are
several differences and additions to the examples throughout.

The class Node represents the instance of a single node. The attribute 'data' represents
the values stored within the node and 'next' represents the pointer to the next node in line.

The class LinkedList has one attribute called 'head'. It specifies the Node at the beginning of the list.
The class ahs several methods providing functionality of interaction with the LinkedList objects.
"""

__author__ = "Robin Wettstaedt"
__contact__ = "robinwettstadt@gmail.com"
__credits__ = "Course: Algorithms and Data Structures - Full Course for Beginners by teamtreehouse.com"
__date__ = "2021/04/18"
__deprecated__ = False
__email__ = "robinwettstadt@gmail.com"
__maintainer__ = "Robin Wettstaedt"
__status__ = "Pre-Alpha"
__version__ = "0.0.1"


class Node:
    """An object for storing a single node of a linked list.
    Models two attributes - data and the pointer to the next node in the list"""
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Data: {self.data}"


class LinkedList:
    """Linked List implementation"""
    head = None

    def __init__(self, head_node):
        self.head = head_node

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            if current_node is self.head:
                nodes.append(f"Head Node: {current_node}")
            elif current_node.next is None:
                nodes.append(f"Tail Node: {current_node}")
            else:
                nodes.append(f"Node: {current_node}")
            current_node = current_node.next
        s = ""
        for node in nodes:
            s = s + f"{node} -> "
        return s

    def append_node(self, data):
        """
        appends a Node to the end of the specified list
        :param data: the data value the new Node shall hold
        :return: None
        """
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def prepend_node(self, data):
        """
        prepends a Node to the list
        new Node will be the .head attribute of the list object
        :param data: the data value the new Node shall hold
        :return: None
        """
        if self.head is None:
            self.head = Node(data)
        else:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head

    def insert_at(self, data, index):
        if index > self.size():
            print("Index out of Bounds.")
            pass
        if index == 0:
            self.prepend_node(data)
        position = 1
        current_node = self.head
        while current_node:
            if index == position:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                pass
            current_node = current_node.next
            position += 1

    def is_empty(self):
        """
        returns state of emptiness as Boolean value
        :param
        :return: Boolean
        """
        return False if self.head else True

    def size(self):
        """
        returns the number of elements inside the given list
        :param
        :return: number of elements inside the given list (Integer)
        """
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def search(self, data):
        """
        searches the given list for the first Node containing given data
        :param data: the data value that is searched for
        :return: Node object / String if no Node found
        """
        position = self.get_index(data)
        current_node = self.head
        while current_node:
            if current_node.data == data:
                print(f"{current_node} at index: {position}")
                return current_node
            current_node = current_node.next
        return "No Node containing requested data."

    def get_index(self, data):
        """
        returns the index of the first Node holding the given data as its value
        :param data: the data value that is searched for
        :return: index of Node (Integer)
        """
        position = 0
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return position
            position += 1
            current_node = current_node.next
        return position

    def remove(self, data):
        """
        removes the first Node in the list containing the given data
        :param data: the data value of the Node to be deleted
        :return: None
        """
        current_node = self.head

        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                    current_node.next = None
            previous_node = current_node
            current_node = current_node.next

    def remove_node_at_index(self, index):
        """
        removes the Node in the list at the specific index
        :param index: position of the Node inside the list
        :return: None
        """
        if index >= self.size():
            print("Index out of Bounds.")
            pass

        current_node = self.head

        if index == 0:
            self.remove(current_node.data)
            pass
        position = 0
        previous_node = current_node
        while current_node:
            if index == position:
                previous_node.next = current_node.next
                current_node.next = None
            previous_node = current_node
            current_node = current_node.next
            position +=1

    def get_node_at_index(self, index):
        """
        returns the Node in the list at the given index position
        :param index: the position of the Node to be retrieved
        :return: Node object
        """
        if index >= self.size():
            print("Index out of Bounds.")
            pass

        current_node = self.head

        if index == 0:
            print(current_node)
            return current_node
        position = 0
        while current_node:
            if index == position:
                print(current_node)
                return current_node
            current_node = current_node.next
            position += 1
