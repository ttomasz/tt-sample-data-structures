"""Sample implementation of a linked list."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, first_node_value):
        self.head = Node(first_node_value)

    def __str__(self):
        return "Linked list - values: " + self.as_list().__str__()

    def as_list(self) -> list:
        """Function returns a list with all the values from the linked list."""
        array = []
        temp = self.head
        while temp:
            array.append(temp.value)
            temp = temp.next
        return array

    def list_of_nodes(self) -> list:
        """Function returns a list of nodes from the linked list."""
        array = []
        temp = self.head
        while temp:
            array.append(temp)
            temp = temp.next
        return array

    def add(self, value):
        """Function adds a new node with given value to the end of the linked list."""
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def remove_last(self):
        """Function removes the last node from the linked list."""
        previous_node = None
        last_node = self.head
        if self.head:
            if last_node.next:
                while last_node.next:
                    previous_node = last_node
                    last_node = last_node.next
                previous_node.next = None
            else:
                self.head = None

    def remove_first(self):
        """Function removes the first element of the linked list."""
        if self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None

    def add_at_the_beginning(self, value):
        """Function adds a new node with given value at the beginning of the linked list
        moving the rest of the values one step further."""
        temp = self.head
        self.head = Node(value)
        self.head.next = temp

    def add_after_node(self, value, node: Node):
        """Function adds a node with given value after specified node."""
        temp = self.head
        while temp:
            if temp == node:
                t1 = temp.next
                temp.next = Node(value)
                temp.next.next = t1
                return
            temp = temp.next
        raise AttributeError("Error. Couldn't find the node.")

    def add_before_node(self, value, node: Node):
        """Function adds a node with given value before specified node."""
        if self.head == node:
            self.add_at_the_beginning(value)
            return
        temp = self.head
        last = None
        while temp:
            if temp == node:
                last.next = Node(value)
                last.next.next = temp
                return
            last = temp
            temp = temp.next
        raise AttributeError("Error. Couldn't find the node.")

    def remove_node(self, node: Node):
        """Function removes given node from the linked list."""
        if self.head == node:
            self.remove_first()
            return
        temp = self.head
        last = None
        while temp:
            if temp == node:
                last.next = temp.next
                return
            last = temp
            temp = temp.next
        raise AttributeError("Error. Couldn't find the node.")
